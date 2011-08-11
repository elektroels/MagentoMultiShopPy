/** Stores n websites **/
/**

INSERT INTO `mc01`.`core_website` (`website_id` ,`code` ,`name` ,`sort_order` ,`default_group_id` ,`is_default`)
VALUES (NULL , 'websitetest', 'websitetest', '0', '0', '0');

 website_id 	code 	name 		sort_order 	default_group_id 	is_default
		0 		admin 	Admin 			0 				0 				0
		1 		base 		Main Website 	0 				1 				1
		2 		troels 	troels 			0 				2			 	0





INSERT INTO `mc01`.`core_store_group` (`group_id` ,`website_id` ,`name` ,`root_category_id` ,`default_store_id`)
VALUES (NULL , '0', 'test', '0', '0');

group_id 	website_id 	name 		root_category_id 	default_store_id
 	0 		0 			Default 			0 			0
 	1 		1 			Main Store 			3 			1
 	2 		2 			troels 				3 			4





store_id 	code 	website_id 	group_id 	name 	sort_order 	is_active
	 	0 		admin 		0 			0 		Admin	 	0 			1
	 	1 		default 	1 			1 		English 	0 			1
		2 		german 		1 			1 		German 		0 			1
	 	3 		french 		1 			1 		French 		0	 		1
	 	4 		troels 		2 			2 		Dansk 		0 			1





insert into core_config_data

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
 	104 	stores 	        4 	general/store_information/name 	troels dansk
 	
**/
