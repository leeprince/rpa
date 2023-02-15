# captcha_qq
# 腾讯防水墙滑动验证码破解
    * 使用OpenCV库
    * 成功率大概90%左右：在实际应用中，登录后可判断当前页面是否有登录成功才会出现的信息：比如用户名等。循环
    * 验证码地址：https://open.captcha.qq.com/online.html
    * 破解 腾讯滑动验证码
    * 腾讯防水墙
    * python + seleniuum + cv2

## 代码在这里

https://github.com/ybsdegit/captcha_qq/blob/master/captcha_qq.py
## 结果展示
![结果](./result/result.gif)


## prince 测试相关
### 尺寸及位置信息
```
获取 遮罩图/裁剪图 元素的尺寸>>>>>
	 web_image_size：{'height': 195, 'width': 341}  # 渲染大小
	 web_image_width：341  # 渲染大小的宽
	 bk_block_x：10  # 元素在可渲染画布中的位置
	 slide_block_x：36 # 元素在可渲染画布中的位置

通过已保存的本地遮罩图/裁剪图，获取位置信息 >>>>>
	 real_width：680  # 图片的真实尺寸：0：宽度；1：高度
	 width_scale：1.9941348973607038  # 图片真实尺寸与渲染大小的比例
	 position：(31, 479)  # 真实滑块背景图片中的｀缺块｀所在的位置  
	 real_scale_position：240.2044117647059  # 渲染滑块背景图片出来后的｀缺块｀所在的位置的横向偏移量(x)
	 real_position：214.2044117647059  # 渲染的页面中应滑动滑块的宽度(x)（slide_block_x > bk_block_x）
	 track_list：[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, -3, -2, -2, -3, -3, -2, -1, -2]
```

