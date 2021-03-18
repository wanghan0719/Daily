import numpy as np
import matplotlib.pyplot as mp
import numpy.fft as nf

n = 1000
y = 0
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
for i in range(1, n + 1):
    y += 4 * np.pi / (2 * i - 1) * np.sin((2 * i - 1) * x)
mp.grid(linestyle=':')
# mp.plot(x, y, color='red', label='y')

# 傅里叶变换拆分
mp.subplot(121)
mp.title('Time Domain')
complex_ary = nf.fft(y)
print(complex_ary.shape, complex_ary[0])
# 逆向傅里叶变换合成
new_y = nf.ifft(complex_ary)
mp.plot(x, new_y, color='red', label='new_y', linewidth=7, alpha=0.3)
mp.grid(linestyle=':')
mp.legend()

# 绘制傅里叶变换后得到的频域图像
freqs = nf.fftfreq(y.size, x[1] - x[0])
pows = np.abs(complex_ary)
mp.subplot(122)
mp.title('Frequency Domain')
mp.plot(freqs[freqs > 0], pows[freqs > 0], color='green', label='freq & pow')
mp.grid(linestyle=':')
mp.legend()
mp.show()

"""
基于傅里叶变换的频域滤波
"""
import scipy.io.wavfile as wf

# 读取音频文件，返回采样率、采样位移
sample_rate, sigs = wf.read('data/noised.wav')
print('采样率：', sample_rate)
print('采样位移：', sigs.shape)

# 1. 绘制音频时域时间/位移图像
times = np.arange(sigs.size) / sample_rate
sigs = sigs / 2 ** 15

mp.figure('Noised Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain')
mp.grid(linestyle=':')
mp.ylabel('sigs', fontsize=14)
mp.plot(times[:178], sigs[:178], color='pink', label='Noised')

# 2. 基于傅里叶变化，获取音频频域信息
complex_ary = nf.fft(sigs)
print(complex_ary.shape)
freqs = nf.fftfreq(sigs.size, times[1] - times[0])
pows = np.abs(complex_ary)
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.grid(linestyle=":")
mp.ylabel('pows', fontsize=14)
mp.semilogy(freqs[freqs > 0], pows[freqs > 0], color='dodgerblue', label='noised freq')  # 采用半对数坐标

# 3. 将低能噪声去除，绘制音频/能量图像
# 找到能量最大的采样点的位置，去除其它的
maxpow_freq = freqs[pows.argmax()]
noised_mask = freqs != maxpow_freq
complex_ary[noised_mask] = 0
pows = np.abs(complex_ary)
mp.subplot(224)
mp.title('Frequency Domain', fontsize=16)
mp.grid(linestyle=":")
mp.ylabel('pows', fontsize=14)
mp.plot(freqs[freqs > 0], pows[freqs > 0], color='orangered', label='filter freq')  # 采用半对数坐标

# 4. 做逆向傅里叶变换，生成降噪后的音频时域图
filter_sigs = nf.ifft(complex_ary)  # 逆向傅里叶变换
mp.subplot(223)
mp.title('Time Domain')
mp.grid(linestyle=':')
mp.ylabel('sigs', fontsize=14)
mp.plot(times[:178], filter_sigs[:178], color='pink', label='Filtered')

# 5. 将降噪后的数组还原成音频
wf.write("data/filtered_777.wav",  # 文件路径
         sample_rate,  # 采样率
         (filter_sigs * 2 ** 15).astype(np.int16))  # 数据

mp.tight_layout()
mp.legend()
mp.show()
