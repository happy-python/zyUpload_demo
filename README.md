## 利用 zyUpload 实现图片的上传
* 在 Django 中使用 ImageField 之前，需要安装 Pillow，不然会报错：Cannot use ImageField because Pillow is not installed.
* 保证 zyFile.js 中 formdata.append(name, file) 和 request.FILES.get(name) 的 name 属性值一样
* 在 initUpload.js 中设置 url
