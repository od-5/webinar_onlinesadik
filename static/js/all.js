$(document).ready(function () {
	
	// fancybox
	jQuery('.fancybox').fancybox();	
	
	// scroll
	$('.scroll').click(function(e){
		e.preventDefault();
		var selected = $(this).attr('href').replace('/', '');
		$.scrollTo(selected, 1000, {offset: -60});
		return false;
	});
	
	
	// animation trigger
	var document_top = $(document).scrollTop();
	var height = $(window).height();
	$('.animate').each(function(){
		var offset = $(this).offset().top - height + height/6;
		if(document_top > offset){
			$(this).addClass('ani_start');
		}else{
			$(this).removeClass('ani_start');
		}
	});
	$(window).scroll( function(e){
		var document_top = $(document).scrollTop();
		var height = $(window).height();
		$('.animate').each(function(){
			var offset = $(this).offset().top - height + height/6;
			if(document_top > offset){
				$(this).addClass('ani_start');
			}else{
				$(this).removeClass('ani_start');
			}
		});
		
	});
	
});