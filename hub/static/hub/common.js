/**
 * Created by zhangyao on 2017/12/7.
 */
//处理csrf
jQuery(document).ajaxSend(function (event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
//正文
$(document).ready(function () {
    window.onload = function () {
        getTestUrls()
        getProdUrls()
    }
    /*****************  通用 开始 ****************/
    //载入中
    function loading(prompt) {
        $('body').append('<div class="centerScreen"><h1>'+prompt+'</h1></div>')
    }

    /*****************  通用 结束 ****************/
    /*****************  操作手机号邮箱 开始 ****************/
    // 点击修改手机号按钮
    $("#prod_updatephone .update_phone_btn").click(function () {
        var result = confirm('确认执行！？');
        if (result) {
            updatephone('prod');
            loading('Processing...')
        } else {
        }
    })
    $("#test_updatephone .update_phone_btn").click(function () {
        var result = confirm('确认执行！？');
        if (result) {
            updatephone('test');
            loading('Processing...')
        } else {
        }
    })
    // todo:修改手机号
    function updatephone(env) {
        var prefix = '';
        if (env === 'test'){
            prefix = '#test_updatephone ';
        }else if (env === 'prod') {
            prefix = '#prod_updatephone ';
        }
        else{
            console.error('argument error: env has to be prod, or ssdd')
        }
        var org_phone = $(prefix+".org_phone").val();
        var new_phone = $(prefix+".new_phone").val();
        var password = $(prefix+".id_password").val();
        $.ajax({
            type: "POST",
            url: "newPhone",
            // contentType: "application/json; charset=utf-8", // 规定了发送数据的类型
            // dataType: "json",  // 规定了返回 数据的类型。
            data: {
                "org_phone": org_phone,
                "new_phone": new_phone,
                "password": password,
                'environment':env
            },
            success: function (result) {
                // 转换Unicode成可以正常显示的中文。
                // result = eval("'" + result + "'");
                // 测试代码
                // alert(result)
                $('.centerScreen').remove();
                alert(result.msg);
            },
            error: function (result) {
                console.error("错误，请稍后再试。");
            }
        });
    }

    /****************  操作手机号邮箱 结束  *****************/
    /****************  页面 开始  *****************/
    //切换页面
    $("#testurls_tab").click(function () {
        $("#container").children(".layer").removeClass("active");
        $(".nav").children("a").removeClass("active");
        $("#testurl_layer").addClass("active");
        $("#testurls_tab").addClass("active");
    });
    $("#produrls_tab").click(function () {
        $("#container").children(".layer").removeClass("active");
        $(".nav").children("a").removeClass("active");
        $("#produrl_layer").addClass("active");
        $("#produrls_tab").addClass("active");
    });
    $("#phone_tab").click(function () {
        $("#container").children(".layer").removeClass(" active");
        $(".nav").children("a").removeClass("active");
        $("#phone_layer").addClass("active");
        $("#phone_tab").addClass("active");
    });
    //请求testurl
    function getTestUrls() {
        $.ajax({
            type: "GET",
            url: "testUrls",
            contentType: "application/json; charset=utf-8", // 规定了发送数据的类型
            // dataType: "json",  // 规定了返回 数据的类型。
            success: function (result) {
                displayUrls(result,"test")
            },
            error: function (result) {
                console.error("错误，请稍后再试。")
            }
        })
    }
    //请求produrl
    function getProdUrls() {
        $.ajax({
            type: "GET",
            url: "prodUrls",
            contentType: "application/json; charset=utf-8", // 规定了发送数据的类型
            // dataType: "json",  // 规定了返回 数据的类型。
            success: function (result) {
                displayUrls(result,"prod")
            },
            error: function (result) {
                console.error("错误，请稍后再试。")
            }
        })
    }

    //把url放到对应表格里
    function displayUrls(urls,env) {
        //判断环境
        var table
        if (env === "test"){
            table = "#test_table>tbody"
        }
        else if(env === "prod"){
            table = "#prod_table>tbody"
        }else {
            console.error("error env passed in displayTestUrls()")
        }

        $.each(urls.theUrls,function (i,item) {
            var $name_index = $("<td>").text(i);
            var $name_str = $("<td>").text(item.name);
            var $url_str = $("<td>").text(item.addr);
            var $update_str = $("<td>").text(item.update);
            var $url_row = $("<tr>").append($name_index)
            $url_row.append($name_str)
            $url_row.append($url_str)
            $url_row.append($update_str)

            $(table).append(
               $url_row
            );
            // $("#test_table.tbody").append(
            //    $url_row
            // );

        })

    }

    /****************  页面 结束  *****************/


})