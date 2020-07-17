//Java.perform(function x() {
//        console.log("Inside java perform function");
//        //定位类
//         //定位类成功！
//        console.log("Java.Use.Successfully!");
//        console.log(MobCommunicator);
//        //在这里更改类的方法的实现（implementation）
////        public <T> T requestSynchronized(boolean z, HashMap<String, String> hashMap, HashMap<String, Object> hashMap2, String str, boolean z2) throws Throwable {
//
////        MobCommunicator.requestSynchronized.overload("java.lang.String").implementation = function(url){
////            console.log(url);
////            return this.loadUrl(url);
////        };
//          MobCommunicator.a.overload("boolean", "java.util.HashMap", "java.lang.String", "int") = function(z, hashMap, str, i){
//                console.log("===========================>")
////              console.log(z);
////              console.log(hashMap);
////              console.log(hashMap2);
////              console.log(str);
////              console.log(z2);
//              return this.requestSynchronized(z, hashMap, str, i);
//          };
//
//    });

//frida -U --no-pause -f com.mksh.tky -l hook.js
Java.perform(function x() {
var hook = Java.use("com.mob.MobCommunicator");
var targetMethod = "requestSynchronized";
var overloadCount = hook[targetMethod].overloads.length;

hook.$init.implementation = function (a,b,c) {
        console.log("Hook Start...");
        console.log("a", a);
        console.log("b", b);
        console.log("c", c);
        return this.$init(a,b,c);
    }

//打印日志：追踪的方法有多少个重载
console.log("Tracing " + targetMethod + " [" + overloadCount + " overload(s)]");
//每个重载都进入一次
    for (var i = 0; i < overloadCount; i++) {
    //hook每一个重载
        hook[targetMethod].overloads[i].implementation = function() {
            console.warn("n*** entered " + targetMethod);

            //可以打印每个重载的调用栈，对调试有巨大的帮助，当然，信息也很多，尽量不要打印，除非分析陷入僵局
            Java.perform(function() {
                 var bt = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
                    console.log("nBacktrace:n" + bt);
            });

            // 打印参数
            if (arguments.length) console.log();
            for (var j = 0; j < arguments.length; j++) {
                console.log("arg[" + j + "]: " + arguments[j]);
            }
            //打印返回值
            var retval = this[targetMethod].apply(this, arguments); // rare crash (Frida bug?)
            console.log("nretval: " + retval);
            console.warn("n*** exiting " + targetMethod);
            return retval;
        }
    }
    });