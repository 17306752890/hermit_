$(function () {
    //右下角鼠标经过变色
    $('.right_bottom1').mouseover(
        function () {
            $(this).addClass('right_mouseover')
        }
    )
    $('.right_bottom1').mouseleave(
        function () {
            $(this).removeClass('right_mouseover')
        }
    )

    //添加评论

    var btnComm=$('.sub')
    btnComm.click(function () {

         var dataShowHtml=$('.remark').html()
        var commentVal=$('.inputComment').val()

        str = '<div class="comment1"> <div>  </div> <div class="link"></div> <div class="lever"> <img src="pic/photo.png" style="width: 47px;height: 47px;"><br> <span>lv.10</span> </div> <div class="content"> <span class="username">user 1</span> <p >'
                         +commentVal +
                     '</p> <img src="pic/content1.jpeg"> <img src="pic/content2.jpeg"> <img src="pic/content3.jpeg"><br> <span>2018-07-16 12:24:57</span> </div>'
        $('.remark').html(dataShowHtml+str)
            commentVal('')
    })

    $('.xx').click(
        function () {
            $('.gg').hide()
            $('.xx').hide()
        }
    )
    //分享
    var sharBtn = $('.right_bottom1 a')
    sharBtn.click(
        function () {
            $('.share').show()
            $('.body').css({'opacity':'0.2'})
            // $('.share').css({'opacity':'1'})
        }
    )
    $('.share_x').click(
        function () {
            $('.share').hide()
            $('.body').css({'opacity':'1'})
        }
    )








})