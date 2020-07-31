import requests
from bs4 import BeautifulSoup, NavigableString
import os

url = "https://www.androidos.net.cn"
html = """
<!DOCTYPE html>
<html lang="zh-cmn-Hans" prefix="og: http://ogp.me/ns#" class="han-init">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="baidu-site-verification" content="q1tMZvbwXu" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />

    <meta name="keywords" content="android os源代码，在线查看，技术文章，Android开发" />
    <meta name="description" content="Android社区提供在线查看系统原代码，及一系列的高质量文章，让您紧跟Android开发的最前线。">

            <title>10.0.0_r6 - Android社区 - https://www.androidos.net.cn/</title>
    <style>
        .breadcrumb{
            padding: 2px 8px;
            background-color: #fff!important;
            padding-bottom: 0px!important;
            margin-bottom: 5px!important;
            padding-left:0px!important;
            margin-left:0px!important;
        }
        .breadcrumb > li + li:before {
            content: "/"!important;
        }

        .filelist{
            border-top: none;
            margin-top: 5px!important;
            background-color: #fff!important;
        }

        .filelist>tbody>tr:nth-of-type(odd) {
            background-color: #fff!important;
        }

        .filelist tr{
            border: none;
        }

        .filelist tr td{
            border: none;
        }

        .icon{
            width: 17px;
            padding-right: 2px;
            padding-left: 10px;
            color: rgba(3,47,98,0.55);
            line-height: 20px;
        }

        .content{
            padding-left: 2px!important;
        }

        .size{
            width: 100px;
        }

        .octicon {
            vertical-align: text-bottom;
            display: inline-block;
            fill: currentColor;
        }

        .contenturl{
            font-size:18px;
            padding-left: 1px!important;
        }
        .quicksearchul{
            list-style: none;
            margin-left:0px;
            padding-left:30px;
        }

        .quicksearchul li{
            list-style: none;
        }
        .quicksearchul li p{
            margin: 0px;padding:0px;
        }

        .list-group{

        }

        .list-group a{
            padding-bottom: 6px!important;
            border-bottom:1px solid #ccc;
            border-radius:0px!important;
        }
        .list-group a:hover{
            border-radius:0px!important;
            text-decoration: none;
            border-bottom:1px solid #ccc;
        }

        .list-group a p{
            margin: 0px;padding:0px;font-size: 17px;
            line-height: 100%;
        }

        .list-group a span{
            margin: 0px;padding:0px;font-size: 15px;color: #ccc;
            line-height: 100%;
        }

        .mytabactive{
            color:#101010!important;font-weight: bold;
        }
        .mytabactive a{
            border-top: 4px solid #101010;
        }
    </style>

    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/vendor/fancybox/source/jquery.fancybox.css?ver=267">
    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/vendor/font-awesome/css/font-awesome.min.css?ver=267">
    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/vendor/font-awesome/css/font-awesome.min.css?ver=267">
    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/css/beauty/bootstrap.min.css?ver=267">
    <link rel="stylesheet" href="/themes/default/css/beauty/index.css?ver=316">
    <link rel="stylesheet" href="/themes/default/css/beauty/androidos.css?ver=316">
    

    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon"/>

    <meta property="og:locale" content="zh_CN" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <script src="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/vendor/jquery/dist/jquery.min.js?ver=267"></script>
    <!--[if lte IE 9]>
    <script type="text/javascript" src="https://oss-cn-hangzhou.aliyuncs.com/codingsky/cdn/default/jquery/1.9.1/jquery.min.js"></script>
    <![endif]-->

    <script src="https://oss-cn-hangzhou.aliyuncs.com/codingsky/cdn/default/bootstrap/js/bootstrap.min.js"></script>

    <script src="https://oss-cn-hangzhou.aliyuncs.com/codingsky/cdn/codingsky/themes/default/toc/jquery.toc.js"></script>
    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/cdn/codingsky/themes/default/toc/toc.css" />

    <link rel="stylesheet" href="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/highlight/styles/github.css?ver=267">
    <script src="https://oss-cn-hangzhou.aliyuncs.com/codingsky/androidos/assets/themes/default/highlight/highlight.min.js?ver=267"></script>

    <script src="/themes/default/js/csk/csk.sdk.min.js?ver=316"></script>
</head>
<body class="home" style="overflow: auto;min-width: 1100px;">

<div class="newcontainer one-collumn sidebar-position-left page-home">
    <nav class="navbar navbar-fixed-top mynav" style="height: 50px!important;box-shadow:0 0 5px #888;">
        <div class="newcontainer">
            <div class="container-fluid" style="padding-left: 0px;">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <a class="navbar-brand alipuhuiti" href="/" style="font-size:30px;border-bottom: 0px;color:rgb(28, 171, 91);padding-left:0px;margin-left:0px;">ANDROID社区</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <form class="navbar-form navbar-left" method="get" action="/androidossearch" style="margin-top: 8px;padding-left:0px!important;padding-right:5px!important;">
                        <div class="form-group">
                            <input type="text" class="form-control newsearchcontrol" id="query" name="query" placeholder="输入文件名,按下回车开始搜索">
                        </div>
                    </form>
                    <ul class="nav navbar-nav">
                        <li class=""><a style="border-bottom: 0px;" href="/sourcecode">源代码</a></li>
                        <li class=""><a style="border-bottom: 0px;" href="/news">资讯</a></li>
                        <li class=""><a style="border-bottom: 0px;" href="/articles">技术文章</a></li>
                        <li class=""><a style="border-bottom: 0px;" href="/snippet">代码片断</a></li>
                        <li class=""><a style="border-bottom: 0px;" href="/tools">工具</a></li>
                    </ul>

                    <div style="float:right;height:54px;line-height:54px;">
                        <ul class="nav navbar-nav">
                            <div id="loginedNavBar" class="dropdown" style="display:none">
                                <a style="border-bottom: 0px;color:#222;display:inline-block;max-width:160px;text-overflow:ellipsis;white-space: nowrap;overflow: hidden;padding-left:5px;padding-right:5px;" href="#" class="dropdown-toggle" id="mydropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"><span id="usernamespan"></span><span class="caret"><span>&nbsp;&nbsp;</span></span></a>
                                <ul class="dropdown-menu" aria-labelledby="mydropdown">
                                    <li><a style="border-bottom: 0px!important;" href="/my/collect/code">我收藏的代码</a></li>
                                    <li><a style="border-bottom: 0px!important;" href="/my/read/code">我读过的代码</a></li>
                                    <li><a style="border-bottom: 0px!important;" href="/my/collect/article">我收藏的文章</a></li>
                                    <li role="separator" class="divider"><div style="background-color: #ccc;height:1px;"></div></li>
                                    <li><a style="border-bottom: 0px!important;" href="/user/logout">退出登录</a></li>
                                </ul>
                            </div>
                            <div id="registerLoginNavBar">
                                <a style="border-bottom: 0px;color:#aaa;" href="/user/register">注册</a>
                                <span>|</span>
                                <a style="border-bottom: 0px;color:#aaa;" href="/user/login">登录</a>
                            </div>
                        </ul>
                    </div>



                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </div>
    </nav>
    <div style="height: 60px;"></div>

    <!-- / header -->
        <div style="background:#fff;">
        <div class="newcontainer" >
            <div class="row">
                <div class="col-md-12">
                    <div style="margin-top: 10px;margin-bottom: 5px;font-size: 20px;padding-left:10px;padding-right:10px;">
                        <a class="cleanurl" href="/android/10.0.0_r6/xref" style="float:left;">Android 10</a>
                        <span style="float:left;">&nbsp;|&nbsp;</span>
                        <a class="cleanurl" href="/android/10.0.0_r6/xref">10.0.0_r6</a>
                        <div style="float: right">
                            <button class="btn btn-default" data-toggle="modal" data-target="#quicksearch" onfocus="this.blur()" onclick="">快速搜索文件</button>
                        </div>
                        <div style="clear: both"></div>
                    </div>
                    <div style="height: 3px;background-color: #eee;margin:15px 10px 15px 10px;"></div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-12">
                <ol class="breadcrumb">
                    <li><a class="cleanurl" style="margin-left:0px;padding-left:8px;" href="/android/10.0.0_r6/xref">根目录</a>:</li>
                                                                                                        <li class="active"></li>
                                                            </ol>
                </div>
            </div>

            
        </div>

        </div>
    </div>

    <div class="newcontainer" style="margin-top:10px;">
    <div class="row">
            <div class="col-md-9">
                <div style="background:#f7f7f7;font-size:14pt;padding-top:6px;padding-left:10px;padding-right:10px;border:1px solid #ccc;border-bottom:0px;">
                    <div style="">
                        <span style="font-size:14px;">24个文件夹&nbsp;,&nbsp;4个文件</span>
                        <button onclick="javascript:addFolderFavourite()" style="float: right;height:25px;margin-top: 3px;" class="btn btn-success"><i class="fa fa-heart-o"></i>收藏此目录</button>
                    </div>
                </div>
                <table class="table table-hover filelist" style="margin-top: 0px!important;border:1px solid #ccc;">
                    <thead style="display: none">
                    <tr style="height: 1px;">
                        <th style="width: 5%"></th>
                        <th style="width: 30%"></th>
                        <th style="width: 45%"></th>
                        <th style="width: 5%"></th>
                        <th style="width: 15%"></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td class="icon"></td>
                        <td class="content" colspan="4"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref">..</a></td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/bootable">bootable</a></td>
                        <td class="desc">启动引导程序的源码</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/bootable">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/bootable">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/dalvik">dalvik</a></td>
                        <td class="desc">dalvik的Java虚拟机
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/dalvik">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/dalvik">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/device">device</a></td>
                        <td class="desc">设备相关代码和编译脚本</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/device">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/device">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/pdk">pdk</a></td>
                        <td class="desc">平台开发套件</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/pdk">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/pdk">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/cts">cts</a></td>
                        <td class="desc">android兼容性测试套件</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/cts">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/cts">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/art">art</a></td>
                        <td class="desc">google在4.4后加入用来代替Dalvik的运行时环境</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/art">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/art">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/sdk">sdk</a></td>
                        <td class="desc">sdk及模拟器</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/sdk">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/sdk">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/toolchain">toolchain</a></td>
                        <td class="desc"></td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/toolchain">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/toolchain">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/libcore">libcore</a></td>
                        <td class="desc">java核心库</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/libcore">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/libcore">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/platform_testing">platform_testing</a></td>
                        <td class="desc"></td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/platform_testing">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/platform_testing">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/bionic">bionic</a></td>
                        <td class="desc">bionic库，Android的基础库
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/bionic">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/bionic">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/packages">packages</a></td>
                        <td class="desc">Android的原生应用程序，App开发者需要重点关注
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/packages">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/packages">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/external">external</a></td>
                        <td class="desc">由其他平台移植过来的项目，对于移植工作是非常好的参考
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/external">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/external">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/frameworks">frameworks</a></td>
                        <td class="desc">应用程序框架层，请仔细阅读此部分代码，对于开发App会有很大帮助
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/frameworks">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/frameworks">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/tools">tools</a></td>
                        <td class="desc"></td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/tools">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/tools">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/developers">developers</a></td>
                        <td class="desc">开发使用的例子</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/developers">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/developers">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/kernel">kernel</a></td>
                        <td class="desc">linux内核
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/kernel">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/kernel">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/libnativehelper">libnativehelper</a></td>
                        <td class="desc">支持android的类库</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/libnativehelper">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/libnativehelper">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/build">build</a></td>
                        <td class="desc">编译和配置所需的脚本和工具
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/build">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/build">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/development">development</a></td>
                        <td class="desc">开发应用程序所需的模板和工具
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/development">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/development">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/prebuilts">prebuilts</a></td>
                        <td class="desc">编译所需要的程序文件，主要包含不同平台下的ARM编译器</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/prebuilts">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/prebuilts">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/hardware">hardware</a></td>
                        <td class="desc">与硬件相关的库，驱动开发相关
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/hardware">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/hardware">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/test">test</a></td>
                        <td class="desc"></td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/test">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/test">目录树</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-directory" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M13 4H7V3c0-.66-.31-1-1-1H1c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V5c0-.55-.45-1-1-1zM6 4H1V3h5v1z"></path></svg>
                        </td>
                        <td class="content"><a class="cleanurl contenturl" href="/android/10.0.0_r6/xref/system">system</a></td>
                        <td class="desc">Android的底层库
</td>
                        <td class="size">-</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/system">打开</a>&nbsp;&nbsp;
                            <a class="cleanurl" target="_blank" href="/android/10.0.0_r6/tree/system">目录树</a>
                        </td>
                    </tr>
                    
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-text" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
                        </td>
                        <td class="content"><a target="_blank" class="cleanurl contenturl" href="/android/10.0.0_r6/xref/Makefile">Makefile</a></td>
                        <td class="desc"></td>
                        <td class="size">92 B</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/download/Makefile">下载</a>&nbsp;&nbsp;
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/Makefile">阅读</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-text" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
                        </td>
                        <td class="content"><a target="_blank" class="cleanurl contenturl" href="/android/10.0.0_r6/xref/nohup.android-10.0.0_r6.out">nohup.android-10.0.0_r6.out</a></td>
                        <td class="desc"></td>
                        <td class="size">1.67 MB</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/download/nohup.android-10.0.0_r6.out">下载</a>&nbsp;&nbsp;
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/nohup.android-10.0.0_r6.out">阅读</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-text" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
                        </td>
                        <td class="content"><a target="_blank" class="cleanurl contenturl" href="/android/10.0.0_r6/xref/Android.bp">Android.bp</a></td>
                        <td class="desc"></td>
                        <td class="size">225 B</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/download/Android.bp">下载</a>&nbsp;&nbsp;
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/Android.bp">阅读</a>
                        </td>
                    </tr>
                                        <tr>
                        <td class="icon">
                            <svg aria-hidden="true" class="octicon octicon-file-text" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"></path></svg>
                        </td>
                        <td class="content"><a target="_blank" class="cleanurl contenturl" href="/android/10.0.0_r6/xref/bootstrap.bash">bootstrap.bash</a></td>
                        <td class="desc"></td>
                        <td class="size">916 B</td>
                        <td>
                            <a class="cleanurl" href="/android/10.0.0_r6/download/bootstrap.bash">下载</a>&nbsp;&nbsp;
                            <a class="cleanurl" href="/android/10.0.0_r6/xref/bootstrap.bash">阅读</a>
                        </td>
                    </tr>
                                        </tbody>
                </table>
            </div>
            <div class="col-md-3" style="padding-left:0px;margin-right:0px;">
                
                <div class="sideblock">
                    <div class="sideblock_head">
                        <p>大家都在读</p>
                    </div>
                    <div class="sideblockconten">
                                                <a class="taglink" href="/android/10.0.0_r6/xref/frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java">Activity管理服务</a>
                                                <a class="taglink" href="/android/10.0.0_r6/xref/frameworks/base/services/core/java/com/android/server/wm/WindowManagerService.java">窗体管理服务</a>
                                                <a class="taglink" href="/android/10.0.0_r6/xref/frameworks/base/services/core/java/com/android/server/pm/PackageManagerService.java">包管理服务</a>
                                                <a class="taglink" href="/android/10.0.0_r6/xref/frameworks/base/services/java/com/android/server/SystemServer.java">系统服务</a>
                                            </div>
                </div>
                            </div>
    </div>

    <div class="modal fade" id="quicksearch" tabindex="-1" role="dialog" aria-labelledby="quicksearchLabel" aria-hidden="true" >
        <div class="modal-dialog">
            <div class="modal-content" style="border-radius:0px!important;line-height:100%;">
                <div style="padding:0px;">
                    <input id="quicksearchtext" name="quicksearchtext" type="text" class="form-control" placeholder="请输入文件名" style="width: 100%;font-size:18px;height:45px;border-radius:0px!important;" />
                </div>
                <div style="padding-left:0px;padding-right:0px;">
                    <div id="quicksearchfiles" name="quicksearchfiles" class="list-group" style="margin-bottom:0px;">
                        <div style="text-align: center;margin: 50px;">
                            <p>请输入文件名以搜索代码,如Activity.java。</p>
                        </div>
                    </div>
                </div>
                <div style="text-align: center;padding-top:15px;padding-bottom:15px;border-top: 1px solid #ccc;margin-top: -1px;">
                    <a id="newtabsearch" name="newtabsearch" href="/androidossearch?query=" class="cleanurl">在新窗口搜索</a>
                </div>
            </div>

            <!-- /.modal-content -->
        </div>
        <!-- /.modal -->
    </div>

    <div class="modal fade" id="addSuccessDialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header" style="padding: 5px 10px;">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">收藏成功</h4>
                </div>
                <div class="modal-body">
                    收藏成功,您可以在我收藏的代码页面中查看,其地址为:<a href="https://www.androidos.net.cn/my/collect/code">https://www.androidos.net.cn/my/collect/code</a>。
                </div>
                <div class="modal-footer" style="padding: 5px 10px;">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                </div>
            </div>
        </div>
    </div>

    </div>

<!-- footer -->
<footer id="footer" class="footer">
    <div class="newcontainer" style="margin-top: 30px;margin-bottom:0px;padding-top:20px;padding-bottom:20px;">
        <div class="row">
            <div class="col-md-4 col-xs-4">
                <p style="margin-bottom:10px;">网站相关</p>
                <ul class="footerul">
                    <li><a href="/about">关于我们 - 理想与情怀,使命与责任</a></li>
                    <li><a href="/feedback">反馈建议或意见</a></li>
                </ul>
            </div>
            <div class="col-md-4 col-xs-4">
                <p style="margin-bottom:10px;">常用链接</p>
                <ul class="footerul">
                    <li><a href="https://www.tuboshu.mobi">土拨鼠 - 互联网工具小站</a></li>
                    <li><a href="https://www.codingsky.com">Android社区 - 汇集优秀技术文章</a></li>
                    <li><a href="https://www.flutterchina.net.cn/">Flutter - 快速构建你的iOS && Android应用</a></li>
                </ul>
            </div>
            <div class="col-md-4 col-xs-4">
                <p style="margin-bottom:10px;">关于</p>
                <p>提供Android系统源代码在线阅读功能,同时我们采集了一些优秀的解读系统的文章并得到作者的援权发布。希望本站能成为您学习Android系统,进行Android开发的良师益友。</p>
            </div>
        </div>
        <div style="height: 20px;"></div>
        <div class="row" style="text-align: center">
            Copyright© 2013-2016 All Rights Reserved 京ICP备13033312号
        </div>
        <div style="height: 20px;"></div>
    </div>
</footer>

<script type="text/javascript" src="http://tajs.qq.com/stats?sId=66376263" charset="UTF-8"></script>

<script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?380ce51c4bbd2d4b173830236254bd66";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();

    //baidu push
    (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
</script>

<!-- 多条广告如下脚本只需引入一次 -->
<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/c.js" async="async" defer="defer" ></script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-108792812-2"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-108792812-2');
</script>
<script src="/themes/default/js/lazyload.js?ver=316"></script>
<script src="/themes/default/js/beauty/beauty.js?ver=316"></script>

    
<script>
        $("#sid").val("10.0.0_r6");

        var quickSearch = $("#quicksearchtext").val();
        $("#quicksearchtext").keyup(
                function() {
                    if (quickSearch != $(this).val()) {
                        quickSearch = $(this).val();
                        $("#newtabsearch").attr("href","/androidossearch?query=" + quickSearch);

                        if(quickSearch == ""){
                            content = "<div style=\"text-align: center;margin: 50px;\"><p>请输入文件名以搜索代码,如Activity.java。</p></div>";
                            $("#quicksearchfiles").html(content);
                        }else{
                            getAndroidFilelist(quickSearch);
                        }
                    }
                });

        var sid = "10.0.0_r6";
        function getAndroidFilelist(searchText){
            $.ajax({
                url:'/quicksearchfile',
                type:'GET', //POST
                async:true, //或false,是否异步
                data:{
                    searchtext:searchText,sid:sid
                },
                timeout:5000,
                dataType:'json',
                success:function(data,textStatus,jqXHR){
                    if(data.code != 0){
                        return;
                    }

                    content = "";
                    files = data.data;
                    if(files.length == 0){
                        content = "<div style=\"text-align: center;margin: 50px;\"><p>搜索结束,未搜索到文件。</p></div>";
                    }else{
                        for(var i= 0;i < files.length;i++){
                            file = files[i];

                            var item = "";
                            var url = "/android/" + sid + "/xref/" + file.filepath;
                            item = "<a href=\"" + url + "\" class=\"list-group-item\">";
                            item = item + "<p>" + file.filename + "</p>";
                            item = item + "<span>" + file.filepath + "</span>";
                            item = item + "</a>";

                            content = content + item;
                        }
                    }

                    $("#quicksearchfiles").html(content);
                },
                error:function(xhr,textStatus){
                },
                complete:function(){
                }
            })
        }

        var sid = "10.0.0_r6";
        var title = "10.0.0_r6";
        var url = "/android/10.0.0_r6/xref";

        function addFolderFavourite(){
            addFavouriteV2(sid,title,url,2,function(status, respData){
                if (respData == null){
                    return
                }

                if(respData.code == 0){
                    $('#addSuccessDialog').modal();
                }else if(respData.code == 202){
                    window.location.href = '/user/login'
                }
            })

            /*$.ajax({
                url:'/api/favourite/add',
                type:'POST',
                async:true,
                data:{
                    ftype:'2',sid:sid,url:url,title:title
                },
                timeout:5000,
                dataType:'json',
                beforeSend:function(xhr){
                },
                success:function(data,textStatus,jqXHR){
                    if(textStatus == "success"){
                        if(data.code == 0){
                            $('#addSuccessDialog').modal();
                        }else if(data.code == 1){
                            window.location.href = '/login'
                        }
                    }
                },
                error:function(xhr,textStatus){
                },
                complete:function(){
                }
            });*/
        }
    </script>


<script>
$(document).ready(function(){
    usercenter.initAuth()
    if(usercenter.isLogined()){
        $("#registerLoginNavBar").hide(); 
        $("#loginedNavBar").show(); 

        $("#usernamespan").text(usercenter.getMyEmail()); 
    }else{
        $("#registerLoginNavBar").show();
        $("#loginedNavBar").hide(); 
    }
});

function logout(){
    usercenter.logout()
    window.location.reload();
}


function postjsonV2(url, data, callback){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST",url,true);
    xmlHttp.onreadystatechange = function(){
        if (xmlHttp.readyState == 4) {
            if (xmlHttp.status == 200) {
                callback(200, JSON.parse(xmlHttp.responseText));
            }else{
                callback(xmlHttp.status, null);
            }
        }
    };
    
    xmlHttp.send(JSON.stringify(data));
}

function addFavouriteV2(sid,title,url,ftype,callback){
    var apiURL = "/api/favourite/add"
    var data = {"token":usercenter.getMyToken(),"sid":sid,"title":title,"url":url,"ftype":parseInt(ftype)}
    postjsonV2(apiURL, data, function(httpStatus, respData){
        if(callback != null){
            callback(httpStatus,respData)
        }
    })
}

</script>

</body>


</html>

"""


def request_android_source(base_url, action, parent_dir, m):
    cur_url = url + action
    print(cur_url)
    respsonse = requests.get(cur_url)
    decode_html(base_url, respsonse.content.decode(), parent_dir, m)


def down_file(url, file_path):
    respsonse = requests.get(url)
    with open(file_path, "wb") as write_f:
        write_f.write(respsonse.content)


def decode_html(base_url, html, parent_dir, m):
    bs = BeautifulSoup(html, 'lxml')
    if bs.tbody:
        for tr in bs.tbody.children:
            if isinstance(tr, NavigableString):
                continue
            content = tr.find(class_="content")
            if not content or not content.a: continue
            if not content.a.has_attr('href'): continue
            href = content.a.get('href')
            desc = tr.find(class_="desc")
            if not desc: continue
            size = tr.find(class_="size")
            if not size: continue
            basename = os.path.basename(href)
            if size.string == '-':  # 目录
                dd = basename[0]
                dd_map = {}
                m[parent_dir] = dd_map
                m[parent_dir]["."] = dd
                dir_ = os.path.join(parent_dir, dd)
                print(dir_)
                if not os.path.exists(dir_):
                    os.makedirs(dir_)
                request_android_source(base_url, href, dir_, dd_map)
                continue
            m[basename] = basename
            basename = os.path.join(parent_dir, basename)
            if os.path.exists(basename): continue
            cleanurl_ls = tr.find_all(class_="cleanurl")
            for cleanurl in cleanurl_ls:
                if not cleanurl.has_attr('href'): continue
                href = cleanurl.get('href')
                if not href: continue
                if href.__contains__('/download/'):
                    try:
                        down_file(base_url + href, basename)
                    except BaseException as e:
                        print(e)
                        pass


ANDROID_Q = "/android/10.0.0_r6/xref"
# android_q.external.autotest.venv.autotest_lib.venv.autotest_lib.venv.autotest_lib.venv.autotest_lib.venv.autotest_lib.venv.autotest_lib.venv.autotest_lib.client.deps.glbench-images.glbench_fixedbad_images.chrome-os-partner-bug-35823
if __name__ == '__main__':
    action = ANDROID_Q
    dirname = 'android_q'
    m = {}
    request_android_source(url, action, dirname, m)
    with open(dirname + ".json", "wb") as write_f:
        write_f.write(str(m))
    # decode_html(url, html, dirname)
# https://www.androidos.net.cn/android/10.0.0_r6/download/bootable/recovery/applypatch/include/applypatch/imgdiff_image.h
# https://www.androidos.net.cn/android/10.0.0_r6/xref/bootable/recovery/applypatch/include/applypatch/imgdiff_image.h
