function hook_webview(){
    console.log("Script loaded successfully ");
    Java.perform(function x() {
        console.log("Inside java perform function");
        //定位类
        var WebView = Java.use("android.webkit.WebView");
         //定位类成功！
        console.log("Java.Use.Successfully!");
        //在这里更改类的方法的实现（implementation）
        WebView.loadUrl.overload("java.lang.String").implementation = function(url){
            console.log(url);
            return this.loadUrl(url);
        };
       var WebViewClient = Java.use("android.webkit.WebViewClient");
          WebViewClient.onPageStarted.implementation = function(view, url, favicon){
              console.log(url);
              return this.onPageStarted(view, url, favicon);
          };
         var CordovaActivity = Java.use("org.apache.cordova.CordovaActivity");
          CordovaActivity.onResume.implementation = function(){
                    var LOG = Java.use("org.apache.cordova.LOG");
                  LOG.setLogLevel(0);
                       return this.onResume();
                   };
         var PluginManager = Java.use("org.apache.cordova.PluginManager");
          PluginManager.exec.implementation = function(str1, str2, str3, str4){
          console.log("=========================================");
                    console.log(str1);
                    console.log(str2);
                    console.log(str3);
                    console.log(str4);
                       return this.exec(str1, str2,str3,str4);
                   };

        var ResProxy = Java.use("com.nowheregames.resproxy.ResProxy");
        ResProxy.NativeStart.implementation = function(str, str2, strArr, str3, assetManager){
          console.log("NativeStart=========================================");
                    console.log(str);
                    console.log(str2);
                    console.log(strArr);
                    console.log(str3);
                       return this.NativeStart(str, str2,strArr,str3, assetManager);
                   };
        ResProxy.DownloadURL.implementation = function(str, str2, i){
          console.log("NativeStart=========================================");
                    console.log(str);
                    console.log(str2);
                    console.log(i);
                       return this.DownloadURL(str, str2,i);
                   };

    });
//
//    my_class.createImage.implementation = function(requestCode,resultCode,data){
//            //打印替换前的参数
//            console.log( "requestCode="+requestCode);
//            console.log( "resultCode="+resultCode);
//            var result=this.createImage(requestCode,resultCode,data);
//            return result;
//        }
//无参数的函数
//                                                   ClassName.func.overload().implementation=function(){
//                                                       //do something
//                                                   }
};
hook_webview();
//frida -U --no-pause -f com.nowheregames.sweetromance.chs -l hook_webview.js