Java.perform(function x(){






});

// frida -U --no-pause -f com.habby.archero -l hook.js
// frida -U --no-pause -f com.asobimo.toramonline -l hook.js

//write_f = open(r"E:\python3\frida\a.log", 'wb')
function hook_native() {

    // Interceptor.attach(Module.findExportByName(null, "dlopen"), {

    //     onEnter:function(args){
    //         this.lib = Memory.readUtf8String(args[0]);
    //         console.log("dlopen called with: " + this.lib);


    //     },onLeave:function(){



    //     }


    // });


    // var module_libc = Process.findModuleByName("libc");
    // var symbols = module_libc.findExportByName("fstatat64");
    var symbols =Module.findExportByName("libc.so", "fstatat64")
    console.log("symbols.address==",symbols);

    if(symbols!=null){
        Interceptor.attach(symbols,{onEnter:function(args){
        var a = Memory.readUtf8String(args[1]);

        console.log("args", a);

        },onLeave:function(ret){
//            console.log("ret==", ret);

        }
    
    
    }); 
    } 
}


/*

hook libc的fopen。fputs。fclose主动调用来写文件
*/
function HookRT(){

    var fopen_addr=Module.findExportByName("libc","fstatat64");
    
    var fopen_addr=Module.findExportByName("libc","fopen");
    var fputs_addr=Module.findExportByName("libc","fputs");
    var fclose_addr=Module.findExportByName("libc","fclose");

    var fopen=new NativeFunction(fopen_addr,"pointer",["pointer","pointer"]);
    var fputs=new NativeFunction(fputs_addr,"int",["pointer","pointer"]);
    var fclose=new NativeFunction(fopen_addr,"int",["pointer"]);

    var filename=Memory.allocUtf8String("/sdcard/reg.dat");
    var file_mode=Memory.allocUtf8String("w+");
    var contents=Memory.allocUtf8String(" write data");

    var file=fopen(filename,file_mode);
    var ret=fputs(contents,file);
    fclose(file);

}


function main() {
    hook_native();
}

setImmediate(main);