

# Pflow_dynamic

利用百度API来完成校园人流量统计工作，并使用时间序列进行预测与性能测试。

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/TroyeJames9/Pflow_dynamic/">
  </a>
  <p align="center">
    <br />
    <a href="https://www.mubu.com/doc/HBnmzNb3PI"><strong>Explore the doc of this project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/TroyeJames9/Pflow_dynamic/blob/main/jupyter/funasr_run_single.ipynb">Start demo</a>
    ·
    <a href="https://github.com/TroyeJames9/Pflow_dynamic/issues">Report bug</a>
    ·
    <a href="https://github.com/TroyeJames9/Pflow_dynamic/issues">Propose new features</a>
    ·
    <a href="https://github.com/TroyeJames9/Pflow_dynamic/releases/">Stable release</a>
  </p>

</p>


 This README.md is for developers
 
## 目录

- [如何开始](#如何开始)
  - [开发前配置要求](#开发前配置要求)
  - [用法](#用法)
- [目录结构](#目录结构)
- [项目规范](#项目规范)
  - [依赖包更新规范](#依赖包更新规范)
  - [代码编写规范](#代码编写规范)
  - [工作内容提交规范](#工作内容提交规范)
- [开发注意事项](#开发注意事项)
- [如何为开源项目做出贡献](#如何为开源项目做出贡献)

### 如何开始

###### **开发前配置要求**

1. **Python 版本：** 该项目需要 Python 3.x。 推荐Python 3.9
2. **视频处理工具：** 该项目需要底层工具ffmpeg，windows系统请参照[本教程](https://phoenixnap.com/kb/ffmpeg-windows)下载，MAC系统请参照[本教程](https://phoenixnap.com/kb/ffmpeg-mac)下载
3. **包依赖关系：** 您可以在requirements.txt 文件中找到所需包的列表。 在终端位于项目根目录运行`pip install -r requirements.txt`。在安装包之前，务必完成ffmpeg的安装与配置。
4. **开发环境：** 使用您首选的代码编辑器或 IDE 设置您的开发环境。 但是，该项目中的某些导入依赖于 PyCharm 中的“源根”设置。 建议使用 PyCharm 以获得最佳功能。在 PyCharm 中，需要将 `Pflow_dynamic/script` 设置为源根目录，以确保脚本正确运行。
5. **数据集：** 由于本项目使用的视频数据集的敏感性，无法公开披露,故提供`video/exp`的视频下载链接提供一个示例视频。

###### **用法**

1. TODO

### 目录结构

```
filetree 
├── config/ # 存放含有敏感信息的ini文件或者其他配置文件
├── video/
│  ├── /{dataset_name}/
│  │  ├── example.mp4 # 校园视频数据集文件命名规范为：YYYYMMDD_<noon/night>_bridge，其他数据集自定
├── pre_video/ # 存放预处理后的视频文件
│  ├── /{dataset_name}/
│  │  ├── example.mp4 # 校园视频数据集文件命名规范为：pre_YYYYMMDD_<noon/night>_bridge，其他数据集自定
├── jupyter/ # 存放ipynb文件
├── script/ # 存放代码文件
│  ├── /setting.py # 所有跨文件全局变量均由该模块计算和分配。
│  ├── /temp/ # 存放个人非正式代码的py文件
│  │  ├── funasr_go.py
│  │  └── ...
├── requirements.txt
├── style_guide.py # 本项目的风格与注释指导

```

### 项目规范

###### 依赖包更新规范
1. 每当在本项目的虚拟环境执行pip install命令时，一旦确定安装的包是本项目所需要的包，需要及时将该包记录在项目根目录的requirements.txt
2. 规范例子  
- 项目需要新的包black，执行pip install的时候要记住这个包的版本号  
![image](https://github.com/TroyeJames9/Pflow_dynamic/blob/main/IMG/require_1.jpg)
- 然后将这个包记录到requirements中，如下  
![image](https://github.com/TroyeJames9/Pflow_dynamic/blob/main/IMG/require_2.jpg)
- 
###### 代码编写规范
1. [注释和文档字符串](https://mubu.com/doc/4v3SAhMn7es#o-9LDwq4Ni1S)
2. [代码自动格式化程序black](https://mubu.com/doc/4v3SAhMn7es#o-oIpzb5N96T)

###### 工作内容提交规范
提交内容内容包括
- 自己所负责的模块 py文件
- py文件所需求的新的文件夹或文件，但不能包含敏感信息
- 更新了的requirements.txt

### 开发注意事项
1. 敏感信息相关：所有敏感的账号信息、数据库配置信息，均需在本地的config文件夹创建config.ini进行存储，然后使用configparser库在脚本读取敏感信息。
2. 已被忽略的目录：config、video、pre_video、jupyter、script/temp 目录均已加入.gitignore。
3. 进行PR之前不能将main分支的更改merge到功能分支上，必须使用rebase来将main分支的更新同步到功能分支上，并且在此过程中可能需要解决冲突，但必须保留main分支的更改并不做任何修改。在此过程中不清楚的请联系troye james。
4. 当开发过程中需要使用路径时，统一使用setting.py文件里的全局变量来获取路径，然后再使用"/"拼接得到你所需的路径。

### 如何为开源项目做出贡献

贡献使开源社区成为学习、灵感和创造力的绝佳场所。 非常感谢您所做的任何贡献。


1. 分叉项目（协作者直接clone即可）
2. 创建您的功能分支（`git checkout -b feature/AmazingFeature`）
3. 提交您的更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 发起拉取请求

### Copyright

The project is licensed under the GNU License. Please refer to the [LICENSE.txt](https://github.com/TroyeJames9/Pflow_dynamic/LICENSE.txt) for details. 

<!-- links -->
[your-project-path]:TroyeJames9/Pflow_dynamic
[contributors-shield]: https://img.shields.io/github/contributors/TroyeJames9/Pflow_dynamic.svg?style=flat-square
[contributors-url]: https://github.com/TroyeJames9/Pflow_dynamic/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TroyeJames9/Pflow_dynamic.svg?style=flat-square
[forks-url]: https://github.com/TroyeJames9/Pflow_dynamic/network/members
[stars-shield]: https://img.shields.io/github/stars/TroyeJames9/Pflow_dynamic.svg?style=flat-square
[stars-url]: https://github.com/TroyeJames9/Pflow_dynamic/stargazers
[issues-shield]: https://img.shields.io/github/issues/TroyeJames9/Pflow_dynamic.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/TroyeJames9/Pflow_dynamic.svg
[license-shield]: https://img.shields.io/github/license/TroyeJames9/Pflow_dynamic.svg?style=flat-square
[license-url]: https://github.com/TroyeJames9/Pflow_dynamic/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian




