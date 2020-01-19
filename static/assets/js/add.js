$(function(){
	$('.mm').find('a:gt(4)').hide();
	$('.fa-angle-double-down').click(function(){
		$(this).parent().find('.fa-angle-double-down').hide();
		$(this).parent().find('.fa-angle-double-up').show();
		$(this).parent().find('a:gt(4)').show();
	})
	$('.fa-angle-double-up').click(function(){
		$(this).parent().find('.fa-angle-double-up').hide();
		$(this).parent().find('.fa-angle-double-down').show();
		$(this).parent().find(' a:gt(4)').hide();
	})
})