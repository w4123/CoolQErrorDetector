# CoolQErrorDetector
及其简易的酷Q运行状态监测器

# 依赖
本脚本只依赖于Python内置库

# 如何使用
1. 安装[Python 3](https://www.python.org/downloads/)(推荐至少Python3.5)
2. 修改main.py前面配置部分中的qq以及邮件信息(需要SMTP服务器，可以自己搭建或者使用QQ邮件等)
3. 将main.py放于含有CQA/CQP.exe的文件夹, 使用python3运行脚本
4. 大功告成! 你会在酷Q掉线/被冻结的时候收到邮件通知
5. (可选)修改main.py中的mail_content, mail_para, mail_subject, mail_sender_nick等条目来自定义邮件内容

# License
Copyright 2019 w4123溯洄

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
