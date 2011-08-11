
/** Stores n websites
Website Name  # http://1.bp.blogspot.com/-o_G5sn1bct8/TiGWupvb4kI/AAAAAAAAAJo/vpmbaHKG5zE/s1600/05%2Bwebsite%2Binfo.png
Store Name    # http://3.bp.blogspot.com/-wig9rpuQMVI/TiGXh29gN9I/AAAAAAAAAJ4/RX1PDijpBpc/s1600/07%2Bsave%2Bstore.png
Store View    # http://1.bp.blogspot.com/-YQ4FZFpR3Uk/TiGYm0jmw3I/AAAAAAAAAKI/mM1W4JbP1zw/s1600/07%2Bsave%2Bstore%2Bview.png
**/

/**
	store_id 	code 	website_id 	group_id 	name 	sort_order 	is_active
	 	0 	admin 	0 	0 	Admin 	0 	1
	 	1 	default 	1 	1 	English 	0 	1
		2 	german 	1 	1 	German 	0 	1
	 	3 	french 	1 	1 	French 	0 	1
	 	4 	troels 	2 	2 	Dansk 	0 	1
**/

/** core_store_group

group_id 	website_id 	name 		root_category_id 	default_store_id
 	0 		0 	Default 			0 			0
 	1 		1 	Main Store 			3 			1
 	2 		2 	troels 				3 			4		**/

/** core_config_data

	 54 	websites 	2 	web/unsecure/base_url       	http://127.0.0.1/mc01/shops/troels/
 	 55 	websites 	2 	web/secure/base_url 	        https://127.0.0.1/mc01/shops/troels/
 	 89 	websites 	2 	web/unsecure/base_skin_url 	http://127.0.0.1/mc01/skin/
 	 90 	websites 	2 	web/unsecure/base_media_url 	http://127.0.0.1/mc01/media/
 	 91 	websites 	2 	web/unsecure/base_js_url 	http://127.0.0.1/mc01/js/
 	 92 	websites 	2 	web/secure/base_skin_url 	https://127.0.0.1/mc01/skin/
 	 93 	websites 	2 	web/secure/base_media_url 	https://127.0.0.1/mc01/media/
 	 94 	websites 	2 	web/secure/base_js_url 	        https://127.0.0.1/mc01/js/
 	 95 	websites 	2 	web/seo/use_rewrites 	        0
	105 	websites 	2 	general/store_information/name 	troels
 	106 	websites 	2 	general/country/default 	DK
 	107 	websites 	2 	web/default/cms_home_page 	home
 	100 	stores 	        4 	web/secure/base_skin_url 	{{secure_base_url}}skin/
 	101 	stores 	        4 	web/secure/base_media_url 	{{secure_base_url}}media/
 	102 	stores 	        4 	web/secure/base_js_url 	        {{secure_base_url}}js/
 	103 	stores 	        4 	web/default/cms_home_page 	home|5
 	104 	stores 	        4 	general/store_information/name 	troels dansk			**/
