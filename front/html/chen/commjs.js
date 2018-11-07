/*��װ����ajax����*/
var com = {


    meajax: function (murl, mdata, success) {
        $.ajax({
            type: "GET",
           
            url: murl, //���ʵ�����
            data: mdata,
            dataType: "jsonp", //���ݸ�ʽ����Ϊjsonp
            jsonp: "callback", //Jquery������֤����������
            jsonpCallback: "successCallback",//回调方法
            success: function (result) { //�ɹ��Ļص�����
                success?success(result):function(){};	
            },
            error: function (e) {
                alert(JSON.stringify(e));
                //alert("nihao");
            }
        });






    }
}