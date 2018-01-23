#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File  : parse_str.py
# @Author: Shuaiyy
# @Date  : 2018/1/21 14:11
# @Desc  : 

import sys
import json
import HTMLParser
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    string =   "{&quot;id&quot;:294226467,&quot;photo&quot;:{&quot;key&quot;:&quot;assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg&quot;,&quot;full&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=560&amp;h=315&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=bf757e356a209d996dd581a1f86f5bee&quot;,&quot;ed&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=352&amp;h=198&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=40875969336ef019be856ea44cff433f&quot;,&quot;med&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=272&amp;h=153&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=15f7713b4acae5680ba171f7b064778b&quot;,&quot;little&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=208&amp;h=117&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=cbf2c4e09a5177b660b418d3bb2fc4ab&quot;,&quot;small&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=160&amp;h=90&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=82d1035eecddb15013b8b79313fda9fa&quot;,&quot;thumb&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=48&amp;h=27&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=d09db8aa25d3e200268cc0055651510f&quot;,&quot;1024x576&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=1024&amp;h=576&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=2ecd410bf68af3bdd8b545ecef8b6f23&quot;,&quot;1536x864&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=1552&amp;h=873&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=921585663be77e620122cee6d4512fb6&quot;},&quot;friends&quot;:[],&quot;is_starred&quot;:false,&quot;is_backing&quot;:false,&quot;permissions&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;star&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/star?signature=1516600567.87898c66ae43073cea62cb8bff5ff4c36cc90cb7&quot;,&quot;message_creator&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/messages?signature=1516600567.609ca51c1984315373f2f35033eb693c457445df&quot;,&quot;project&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467?signature=1516600567.5151a00077bc75de9215ef816e75a2641fec47b7&quot;,&quot;comments&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/comments?signature=1516600567.337054d078c30beb299095188bf313d6801504bc&quot;,&quot;updates&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/updates?signature=1516600567.fd3f5f30be889674f664de9a2bf436f525f2f281&quot;},&quot;web&quot;:{&quot;message_creator&quot;:&quot;https://www.kickstarter.com/projects/1418490262/losing-the-ratrace/messages/new?message%5Bto%5D=1418490262&quot;,&quot;project&quot;:&quot;https://www.kickstarter.com/projects/1418490262/losing-the-ratrace&quot;,&quot;rewards&quot;:&quot;https://www.kickstarter.com/projects/1418490262/losing-the-ratrace/rewards&quot;,&quot;project_short&quot;:&quot;http://kck.st/1oL10Eh&quot;,&quot;updates&quot;:&quot;https://www.kickstarter.com/projects/1418490262/losing-the-ratrace/posts&quot;}},&quot;name&quot;:&quot;Losing the Ratrace&quot;,&quot;blurb&quot;:&quot;My wife and I are tired of the Ratrace. We&#39;re going off-grid in the Texas Desert and want to document our transition.&quot;,&quot;goal&quot;:4000.0,&quot;pledged&quot;:130.0,&quot;state&quot;:&quot;failed&quot;,&quot;slug&quot;:&quot;losing-the-ratrace&quot;,&quot;disable_communication&quot;:false,&quot;country&quot;:&quot;US&quot;,&quot;currency&quot;:&quot;USD&quot;,&quot;currency_symbol&quot;:&quot;$&quot;,&quot;currency_trailing_code&quot;:true,&quot;deadline&quot;:1407968995,&quot;state_changed_at&quot;:1407969011,&quot;created_at&quot;:1404865938,&quot;launched_at&quot;:1405031395,&quot;staff_pick&quot;:false,&quot;is_starrable&quot;:false,&quot;backers_count&quot;:4,&quot;static_usd_rate&quot;:1.0,&quot;usd_pledged&quot;:&quot;130.0&quot;,&quot;converted_pledged_amount&quot;:130,&quot;fx_rate&quot;:1.0,&quot;current_currency&quot;:&quot;USD&quot;,&quot;usd_type&quot;:&quot;international&quot;,&quot;creator&quot;:{&quot;id&quot;:1418490262,&quot;name&quot;:&quot;Chad Douglas&quot;,&quot;is_registered&quot;:true,&quot;chosen_currency&quot;:null,&quot;avatar&quot;:{&quot;thumb&quot;:&quot;https://ksr-ugc.imgix.net/assets/008/982/169/2ce710e544a84d81df0433538f9d287d_original.jpg?w=40&amp;h=40&amp;fit=crop&amp;v=1461552519&amp;auto=format&amp;q=92&amp;s=e47c92ce4bcec3fbb2105fec70459470&quot;,&quot;small&quot;:&quot;https://ksr-ugc.imgix.net/assets/008/982/169/2ce710e544a84d81df0433538f9d287d_original.jpg?w=160&amp;h=160&amp;fit=crop&amp;v=1461552519&amp;auto=format&amp;q=92&amp;s=1a200d9e54838af544b35614884a82b6&quot;,&quot;medium&quot;:&quot;https://ksr-ugc.imgix.net/assets/008/982/169/2ce710e544a84d81df0433538f9d287d_original.jpg?w=160&amp;h=160&amp;fit=crop&amp;v=1461552519&amp;auto=format&amp;q=92&amp;s=1a200d9e54838af544b35614884a82b6&quot;},&quot;urls&quot;:{&quot;web&quot;:{&quot;user&quot;:&quot;https://www.kickstarter.com/profile/1418490262&quot;},&quot;api&quot;:{&quot;user&quot;:&quot;https://api.kickstarter.com/v1/users/1418490262?signature=1516600567.3469f9ca810e49af0bf7971fbcf92787ab0ed1c1&quot;}}},&quot;location&quot;:{&quot;id&quot;:28747598,&quot;name&quot;:&quot;Salt Flat&quot;,&quot;slug&quot;:&quot;salt-flat-hudspeth-tx&quot;,&quot;short_name&quot;:&quot;Salt Flat, TX&quot;,&quot;displayable_name&quot;:&quot;Salt Flat, TX&quot;,&quot;localized_name&quot;:&quot;Salt Flat&quot;,&quot;country&quot;:&quot;US&quot;,&quot;state&quot;:&quot;TX&quot;,&quot;type&quot;:&quot;Town&quot;,&quot;is_root&quot;:false,&quot;urls&quot;:{&quot;web&quot;:{&quot;discover&quot;:&quot;https://www.kickstarter.com/discover/places/salt-flat-hudspeth-tx&quot;,&quot;location&quot;:&quot;https://www.kickstarter.com/locations/salt-flat-hudspeth-tx&quot;},&quot;api&quot;:{&quot;nearby_projects&quot;:&quot;https://api.kickstarter.com/v1/discover?signature=1516600567.a9300bc85c8c181e1fa8fd4679eee35a055fbda8&amp;woe_id=28747598&quot;}}},&quot;category&quot;:{&quot;id&quot;:48,&quot;name&quot;:&quot;Nonfiction&quot;,&quot;slug&quot;:&quot;publishing/nonfiction&quot;,&quot;position&quot;:9,&quot;parent_id&quot;:18,&quot;color&quot;:14867664,&quot;urls&quot;:{&quot;web&quot;:{&quot;discover&quot;:&quot;http://www.kickstarter.com/discover/categories/publishing/nonfiction&quot;}}},&quot;profile&quot;:{&quot;id&quot;:1133086,&quot;project_id&quot;:1133086,&quot;state&quot;:&quot;inactive&quot;,&quot;state_changed_at&quot;:1425915863,&quot;name&quot;:null,&quot;blurb&quot;:null,&quot;background_color&quot;:null,&quot;text_color&quot;:null,&quot;link_background_color&quot;:null,&quot;link_text_color&quot;:null,&quot;link_text&quot;:null,&quot;link_url&quot;:null,&quot;show_feature_image&quot;:false,&quot;background_image_opacity&quot;:0.8,&quot;should_show_feature_image_section&quot;:true,&quot;feature_image_attributes&quot;:{&quot;image_urls&quot;:{&quot;default&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=1552&amp;h=873&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=921585663be77e620122cee6d4512fb6&quot;,&quot;baseball_card&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/757/759/1c649be41cf16eb9c79a139ba5acb9c8_original.jpg?crop=faces&amp;w=560&amp;h=315&amp;fit=crop&amp;v=1463690528&amp;auto=format&amp;q=92&amp;s=bf757e356a209d996dd581a1f86f5bee&quot;}}},&quot;spotlight&quot;:false,&quot;updated_at&quot;:1407969011,&quot;failed_at&quot;:1407969011,&quot;video&quot;:{&quot;id&quot;:412616,&quot;status&quot;:&quot;successful&quot;,&quot;high&quot;:&quot;https://ksr-video.imgix.net/projects/1107567/video-412616-h264_high.mp4&quot;,&quot;base&quot;:&quot;https://ksr-video.imgix.net/projects/1107567/video-412616-h264_base.mp4&quot;,&quot;webm&quot;:&quot;https://ksr-video.imgix.net/projects/1107567/video-412616-webm.webm&quot;,&quot;width&quot;:640,&quot;height&quot;:360,&quot;frame&quot;:&quot;https://d15chbti7ht62o.cloudfront.net/projects/1107567/video-412616-h264_high.jpg?2014&quot;},&quot;comments_count&quot;:0,&quot;updates_count&quot;:0,&quot;rewards&quot;:[{&quot;id&quot;:0,&quot;description&quot;:&quot;No Reward&quot;,&quot;minimum&quot;:1,&quot;reward&quot;:&quot;No Reward&quot;},{&quot;id&quot;:2848816,&quot;minimum&quot;:1.0,&quot;reward&quot;:&quot;I will personally write your name on a yellow post-it note and stick it somewhere in our cabin. After it has been there long enough to infuse the structure with your awesomeness, I will take it down and burn it.&quot;,&quot;description&quot;:&quot;I will personally write your name on a yellow post-it note and stick it somewhere in our cabin. After it has been there long enough to infuse the structure with your awesomeness, I will take it down and burn it.&quot;,&quot;title_for_backing_tier&quot;:&quot;$1 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874935,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848816?signature=1516600567.41d8470c1af2f86f203ba53d15394a0183e6f232&quot;}}},{&quot;id&quot;:2848860,&quot;minimum&quot;:2.0,&quot;reward&quot;:&quot;I will personally write your name on an ORANGE post-it note and stick it somewhere in our cabin. After it has been there long enough to infuse the structure with your awesomeness, I will take it down and burn it.&quot;,&quot;description&quot;:&quot;I will personally write your name on an ORANGE post-it note and stick it somewhere in our cabin. After it has been there long enough to infuse the structure with your awesomeness, I will take it down and burn it.&quot;,&quot;title_for_backing_tier&quot;:&quot;$2 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874935,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848860?signature=1516600567.f61b26bce450b4957697c9bfeeca4da001449d0d&quot;}}},{&quot;id&quot;:2848884,&quot;minimum&quot;:3.0,&quot;reward&quot;:&quot;I will personally say your name whiile dancing around the campfire in which I am burning the $1 and $2 backers&#39; post-its.&quot;,&quot;description&quot;:&quot;I will personally say your name whiile dancing around the campfire in which I am burning the $1 and $2 backers&#39; post-its.&quot;,&quot;title_for_backing_tier&quot;:&quot;$3 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874935,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848884?signature=1516600567.72eadfd8b357a172917ee58fd4cfaf502d0509ce&quot;}}},{&quot;id&quot;:2848901,&quot;minimum&quot;:5.0,&quot;reward&quot;:&quot;I I will personally say your name whiile dancing around the campfire in which I am burning the $1 and $2 backers&#39; post-its. You will also receive a link to the video of my silliness.&quot;,&quot;description&quot;:&quot;I I will personally say your name whiile dancing around the campfire in which I am burning the $1 and $2 backers&#39; post-its. You will also receive a link to the video of my silliness.&quot;,&quot;title_for_backing_tier&quot;:&quot;$5 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:1,&quot;updated_at&quot;:1486315534,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848901?signature=1516600567.3a710f8006dd8d266f26002f72d4107310b32111&quot;}}},{&quot;id&quot;:2848732,&quot;minimum&quot;:10.0,&quot;reward&quot;:&quot;You will receive a \\&quot;Thank You\\&quot; email with a photo from one of us.&quot;,&quot;description&quot;:&quot;You will receive a \\&quot;Thank You\\&quot; email with a photo from one of us.&quot;,&quot;title_for_backing_tier&quot;:&quot;$10 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874933,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848732?signature=1516600567.6976c4d00af688b575b2fd0670551a24452b7f56&quot;}}},{&quot;id&quot;:2848863,&quot;minimum&quot;:25.0,&quot;reward&quot;:&quot;I will personally write your name on a piece of tissue paper and then eat the tissue.  I will send you photographic proof.&quot;,&quot;description&quot;:&quot;I will personally write your name on a piece of tissue paper and then eat the tissue.  I will send you photographic proof.&quot;,&quot;title_for_backing_tier&quot;:&quot;$25 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:1,&quot;updated_at&quot;:1486315793,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2848863?signature=1516600567.39638972d0929883118c3152c31227aee7d93987&quot;}}},{&quot;id&quot;:2815975,&quot;minimum&quot;:50.0,&quot;reward&quot;:&quot;You will be sent a monthly e-newsletter for one year starting in September 2014, detailing our progress, and full color photographs of our exploits.&quot;,&quot;description&quot;:&quot;You will be sent a monthly e-newsletter for one year starting in September 2014, detailing our progress, and full color photographs of our exploits.&quot;,&quot;title_for_backing_tier&quot;:&quot;$50 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:true,&quot;shipping_preference&quot;:&quot;restricted&quot;,&quot;shipping_summary&quot;:&quot;Only United States&quot;,&quot;estimated_delivery_on&quot;:1409529600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:2,&quot;updated_at&quot;:1486323711,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2815975?signature=1516600567.160042df16b33e82fc78443753417c08d6ae72c2&quot;}}},{&quot;id&quot;:2815973,&quot;minimum&quot;:100.0,&quot;reward&quot;:&quot;You get everything from the $50 level, and we will send you a one-pint mason jar of honest-to-goodness West-Texas desert soil. Yeah, we know it&#39;s worthless, but it will let you show others that you support The Ratrace Losers.&quot;,&quot;description&quot;:&quot;You get everything from the $50 level, and we will send you a one-pint mason jar of honest-to-goodness West-Texas desert soil. Yeah, we know it&#39;s worthless, but it will let you show others that you support The Ratrace Losers.&quot;,&quot;title_for_backing_tier&quot;:&quot;$100 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:true,&quot;shipping_preference&quot;:&quot;restricted&quot;,&quot;shipping_summary&quot;:&quot;Only United States&quot;,&quot;estimated_delivery_on&quot;:1414800000,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874434,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2815973?signature=1516600567.1b5ac4a0cc5b90096f67831aad0fe6c9c134a432&quot;}}},{&quot;id&quot;:2816522,&quot;minimum&quot;:275.0,&quot;reward&quot;:&quot;You will receive everything from the $100 level, and you will also receive private links to YouTube videos of our progress every 4 to 6 weeks for a year.&quot;,&quot;description&quot;:&quot;You will receive everything from the $100 level, and you will also receive private links to YouTube videos of our progress every 4 to 6 weeks for a year.&quot;,&quot;title_for_backing_tier&quot;:&quot;$275 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1412121600,&quot;project_id&quot;:294226467,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874440,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2816522?signature=1516600567.d5b0f147d9fe8e8fbb87fe671ea4dc0f0aeabd8c&quot;}}},{&quot;id&quot;:2816521,&quot;minimum&quot;:750.0,&quot;reward&quot;:&quot;You will get everything from the $275 level, and we will send you a hand-made, hand crafted item.  This could be a pair of woolen socks or even a small woven shawl. We will contact you to see what your preferences and sizes are.&quot;,&quot;description&quot;:&quot;You will get everything from the $275 level, and we will send you a hand-made, hand crafted item.  This could be a pair of woolen socks or even a small woven shawl. We will contact you to see what your preferences and sizes are.&quot;,&quot;limit&quot;:10,&quot;title_for_backing_tier&quot;:&quot;$750 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:true,&quot;shipping_preference&quot;:&quot;restricted&quot;,&quot;shipping_summary&quot;:&quot;Only United States&quot;,&quot;estimated_delivery_on&quot;:1441065600,&quot;project_id&quot;:294226467,&quot;remaining&quot;:10,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874441,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2816521?signature=1516600567.bec03dfa8cb1dae3aab3616f8526d3cae6d623c0&quot;}}},{&quot;id&quot;:2815974,&quot;minimum&quot;:2000.0,&quot;reward&quot;:&quot;You will be invited to come visit our property for a week, where you can camp out under the desert stars.  You can learn what you need to do to get out on your own, and lose your own ratrace.&quot;,&quot;description&quot;:&quot;You will be invited to come visit our property for a week, where you can camp out under the desert stars.  You can learn what you need to do to get out on your own, and lose your own ratrace.&quot;,&quot;limit&quot;:10,&quot;title_for_backing_tier&quot;:&quot;$2,000 reward&quot;,&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1441065600,&quot;project_id&quot;:294226467,&quot;remaining&quot;:10,&quot;backers_count&quot;:0,&quot;updated_at&quot;:1413874434,&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/294226467/rewards/2815974?signature=1516600567.d9f4f32d3d406a315f385db53ba9d833144adb5e&quot;}}}],&quot;items&quot;:[],&quot;livestreams&quot;:[]}"
    string = "{&quot;id&quot;:718749111,&quot;photo&quot;:{" \
             "&quot;key&quot;:&quot;assets/011/418/809/bd5026dbc795b021d5013ee86042d25e_original.png&quot;," \
             "&quot;full&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=560&amp;h=315&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=ace21bd21101db50ce997d58e10e0167&quot;," \
             "&quot;ed&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=352&amp;h=198&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=c783e1ec93fc2d89bd8770f24e972aab&quot;," \
             "&quot;med&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=272&amp;h=153&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=def932587e57732747e8e27176742638&quot;," \
             "&quot;little&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=208&amp;h=117&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=b730a48cce7d909bed687357db520ddb&quot;," \
             "&quot;small&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=160&amp;h=90&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=95950022b44de2825f32dfba40195b07&quot;," \
             "&quot;thumb&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=48&amp;h=27&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=49d0478f878f85c8c6dfda617c03992a&quot;," \
             "&quot;1024x576&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=1024&amp;h=576&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=14adb6ad27095c0b41d86128bd6c71c0&quot;," \
             "&quot;1536x864&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=1552&amp;h=873&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=923517c4a59209ac7cc75f251055ef9e&quot;}," \
             "&quot;name&quot;:&quot;&#39;RADDDDD&#39; A POETRY // SHORT STORY ///  ILLUSTRATION BOOK&quot;," \
             "&quot;blurb&quot;:&quot;LETS PRINT MY FIRST POETRY / SHORT STORY /  ILLUSTRATION BOOK " \
             "&#39;RADDDDD&#39;&quot;,&quot;goal&quot;:1000.0,&quot;pledged&quot;:2453.92," \
             "&quot;state&quot;:&quot;successful&quot;," \
             "&quot;slug&quot;:&quot;raddddd-a-poetry-short-story-illustration-book&quot;," \
             "&quot;disable_communication&quot;:false,&quot;country&quot;:&quot;US&quot;," \
             "&quot;currency&quot;:&quot;USD&quot;,&quot;currency_symbol&quot;:&quot;$&quot;," \
             "&quot;currency_trailing_code&quot;:true,&quot;deadline&quot;:1349067540," \
             "&quot;state_changed_at&quot;:1349067542,&quot;created_at&quot;:1346259018," \
             "&quot;launched_at&quot;:1346789193,&quot;staff_pick&quot;:false,&quot;is_starrable&quot;:false," \
             "&quot;backers_count&quot;:122,&quot;static_usd_rate&quot;:1.0," \
             "&quot;usd_pledged&quot;:&quot;2453.92&quot;,&quot;converted_pledged_amount&quot;:2453," \
             "&quot;fx_rate&quot;:1.0,&quot;current_currency&quot;:&quot;USD&quot;," \
             "&quot;usd_type&quot;:&quot;international&quot;,&quot;creator&quot;:{&quot;id&quot;:1407233593," \
             "&quot;name&quot;:&quot;Daniel Alexander&quot;,&quot;slug&quot;:&quot;snckpck&quot;," \
             "&quot;is_registered&quot;:true,&quot;chosen_currency&quot;:null,&quot;avatar&quot;:{" \
             "&quot;thumb&quot;:&quot;https://ksr-ugc.imgix.net/assets/006/690/532" \
             "/6461d9b27fdbc1f3beba5b6bbac5daaf_original.JPG?w=40&amp;h=40&amp;fit=crop&amp;v=1461404905&amp;auto" \
             "=format&amp;q=92&amp;s=c5ca298f86b1e7fd5d928b2e92bb5221&quot;," \
             "&quot;small&quot;:&quot;https://ksr-ugc.imgix.net/assets/006/690/532" \
             "/6461d9b27fdbc1f3beba5b6bbac5daaf_original.JPG?w=160&amp;h=160&amp;fit=crop&amp;v=1461404905&amp;auto" \
             "=format&amp;q=92&amp;s=82d945f5858ab2dcd6fc37da577633aa&quot;," \
             "&quot;medium&quot;:&quot;https://ksr-ugc.imgix.net/assets/006/690/532" \
             "/6461d9b27fdbc1f3beba5b6bbac5daaf_original.JPG?w=160&amp;h=160&amp;fit=crop&amp;v=1461404905&amp;auto" \
             "=format&amp;q=92&amp;s=82d945f5858ab2dcd6fc37da577633aa&quot;},&quot;urls&quot;:{&quot;web&quot;:{" \
             "&quot;user&quot;:&quot;https://www.kickstarter.com/profile/snckpck&quot;},&quot;api&quot;:{" \
             "&quot;user&quot;:&quot;https://api.kickstarter.com/v1/users/1407233593?signature=1516599830" \
             ".c432e9a9ccb8f1fcc8531656e3ff4bafaf4d0113&quot;}}},&quot;location&quot;:{&quot;id&quot;:2406080," \
             "&quot;name&quot;:&quot;Fort Worth&quot;,&quot;slug&quot;:&quot;fort-worth-tarrant-tx&quot;," \
             "&quot;short_name&quot;:&quot;Fort Worth, TX&quot;,&quot;displayable_name&quot;:&quot;Fort Worth, " \
             "TX&quot;,&quot;localized_name&quot;:&quot;Fort Worth&quot;,&quot;country&quot;:&quot;US&quot;," \
             "&quot;state&quot;:&quot;TX&quot;,&quot;type&quot;:&quot;Town&quot;,&quot;is_root&quot;:false," \
             "&quot;urls&quot;:{&quot;web&quot;:{" \
             "&quot;discover&quot;:&quot;https://www.kickstarter.com/discover/places/fort-worth-tarrant-tx&quot;," \
             "&quot;location&quot;:&quot;https://www.kickstarter.com/locations/fort-worth-tarrant-tx&quot;}," \
             "&quot;api&quot;:{&quot;nearby_projects&quot;:&quot;https://api.kickstarter.com/v1/discover?signature" \
             "=1516577495.175f01a206f7c5bfac8f70e76e093065ef59fb58&amp;woe_id=2406080&quot;}}},&quot;category&quot;:{" \
             "&quot;id&quot;:50,&quot;name&quot;:&quot;Poetry&quot;,&quot;slug&quot;:&quot;publishing/poetry&quot;," \
             "&quot;position&quot;:11,&quot;parent_id&quot;:18,&quot;color&quot;:14867664,&quot;urls&quot;:{" \
             "&quot;web&quot;:{&quot;discover&quot;:&quot;http://www.kickstarter.com/discover/categories/publishing" \
             "/poetry&quot;}}},&quot;profile&quot;:{&quot;id&quot;:322132,&quot;project_id&quot;:322132," \
             "&quot;state&quot;:&quot;inactive&quot;,&quot;state_changed_at&quot;:1425915817,&quot;name&quot;:null," \
             "&quot;blurb&quot;:null,&quot;background_color&quot;:null,&quot;text_color&quot;:null," \
             "&quot;link_background_color&quot;:null,&quot;link_text_color&quot;:null,&quot;link_text&quot;:null," \
             "&quot;link_url&quot;:null,&quot;show_feature_image&quot;:false," \
             "&quot;background_image_opacity&quot;:0.8,&quot;should_show_feature_image_section&quot;:true," \
             "&quot;feature_image_attributes&quot;:{&quot;image_urls&quot;:{" \
             "&quot;default&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=1552&amp;h=873&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=923517c4a59209ac7cc75f251055ef9e&quot;," \
             "&quot;baseball_card&quot;:&quot;https://ksr-ugc.imgix.net/assets/011/418/809" \
             "/bd5026dbc795b021d5013ee86042d25e_original.png?crop=faces&amp;w=560&amp;h=315&amp;fit=crop&amp;v" \
             "=1463682409&amp;auto=format&amp;q=92&amp;s=ace21bd21101db50ce997d58e10e0167&quot;}}}," \
             "&quot;spotlight&quot;:true,&quot;urls&quot;:{&quot;web&quot;:{" \
             "&quot;project&quot;:&quot;https://www.kickstarter.com/projects/snckpck/raddddd-a-poetry-short-story" \
             "-illustration-book&quot;,&quot;rewards&quot;:&quot;https://www.kickstarter.com/projects/snckpck/raddddd" \
             "-a-poetry-short-story-illustration-book/rewards&quot;," \
             "&quot;project_short&quot;:&quot;http://kck.st/TWnHU0&quot;," \
             "&quot;updates&quot;:&quot;https://www.kickstarter.com/projects/snckpck/raddddd-a-poetry-short-story" \
             "-illustration-book/posts&quot;},&quot;api&quot;:{" \
             "&quot;project&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111?signature=1516599830" \
             ".8d374226320417f5c5b978659e6162073edeb2b7&quot;," \
             "&quot;comments&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/comments?signature" \
             "=1516599830.c95c2df636340b39226a02b7a54a77f5812c1c59&quot;," \
             "&quot;updates&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/updates?signature" \
             "=1516599830.c4aa2faeae586231aa11266d9242801a4f2a8fbb&quot;}},&quot;updated_at&quot;:1463682409," \
             "&quot;successful_at&quot;:1349067542,&quot;video&quot;:{&quot;id&quot;:155875," \
             "&quot;status&quot;:&quot;successful&quot;," \
             "&quot;high&quot;:&quot;https://ksr-video.imgix.net/projects/314854/video-155875-h264_high.mp4&quot;," \
             "&quot;base&quot;:&quot;https://ksr-video.imgix.net/projects/314854/video-155875-h264_base.mp4&quot;," \
             "&quot;webm&quot;:null,&quot;width&quot;:640,&quot;height&quot;:360," \
             "&quot;frame&quot;:&quot;https://d15chbti7ht62o.cloudfront.net/projects/314854/video-155875-h264_high" \
             ".jpg?2012&quot;},&quot;comments_count&quot;:5,&quot;updates_count&quot;:14,&quot;rewards&quot;:[{" \
             "&quot;id&quot;:0,&quot;description&quot;:&quot;No Reward&quot;,&quot;minimum&quot;:1," \
             "&quot;reward&quot;:&quot;No Reward&quot;},{&quot;id&quot;:1006232,&quot;minimum&quot;:10.0," \
             "&quot;reward&quot;:&quot;›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››ADD $3 FOR " \
             "INTERNATIONAL SHIPPING‹‹‹\\\\\\\\(ONLY PERTAINS TO THIS OPTION)\\\\\\\\&quot;," \
             "&quot;description&quot;:&quot;›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››ADD $3 FOR " \
             "INTERNATIONAL SHIPPING‹‹‹\\\\\\\\(ONLY PERTAINS TO THIS OPTION)\\\\\\\\&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$10 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:43,&quot;updated_at&quot;:1485564632," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006232?signature" \
             "=1516599830.7ca06c061ca503b3f7c5c6994a71421b53d1b60b&quot;}}},{&quot;id&quot;:1006288," \
             "&quot;minimum&quot;:15.0,&quot;reward&quot;:&quot;›››5 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››5 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$15 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:42,&quot;updated_at&quot;:1506540846," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006288?signature" \
             "=1516599830.002d206768f33b0c2fd6224c83f1931756502aa3&quot;}}},{&quot;id&quot;:1006306," \
             "&quot;minimum&quot;:25.0,&quot;reward&quot;:&quot;›››LIMITED EDITION 2 SIDED RADDDDD/SNCKPCK " \
             "POSTER‹‹‹‹\\r\\n›››10 ‘SNCKPCK’ STICKERS [NEW DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN " \
             "LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR " \
             "NAME IN THE BOOK AS A SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE " \
             "INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;,&quot;description&quot;:&quot;›››LIMITED EDITION 2 SIDED RADDDDD/SNCKPCK " \
             "POSTER‹‹‹‹\\r\\n›››10 ‘SNCKPCK’ STICKERS [NEW DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN " \
             "LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR " \
             "NAME IN THE BOOK AS A SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE " \
             "INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;,&quot;title_for_backing_tier&quot;:&quot;$25 reward&quot;," \
             "&quot;starts_at&quot;:0,&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false," \
             "&quot;estimated_delivery_on&quot;:1351728000,&quot;project_id&quot;:718749111," \
             "&quot;backers_count&quot;:11,&quot;updated_at&quot;:1485561246,&quot;rewards_items&quot;:[]," \
             "&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006306?signature" \
             "=1516599830.af75b34517904d7e5fe8239abb3b154944838864&quot;}}},{&quot;id&quot;:1006309," \
             "&quot;minimum&quot;:35.0,&quot;reward&quot;:&quot;›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTER‹‹‹‹\\r\\n›››10 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTER‹‹‹‹\\r\\n›››10 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹\\r\\n›››SIGNED COPY OF THE BOOK " \
             "&#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$35 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:12,&quot;updated_at&quot;:1485564358," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006309?signature" \
             "=1516599830.7dcf422d167c7ed81bd0932d475da8e140e3e221&quot;}}},{&quot;id&quot;:1006315," \
             "&quot;minimum&quot;:45.0,&quot;reward&quot;:&quot;›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$45 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:1,&quot;updated_at&quot;:1485548021," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006315?signature" \
             "=1516599830.eb118d39ed04d8daab145b68effbe16a74a8e531&quot;}}},{&quot;id&quot;:1006318," \
             "&quot;minimum&quot;:50.0,&quot;reward&quot;:&quot;›››SURPRISE MAIL EVERY MONTH FOR A " \
             "YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››SURPRISE MAIL EVERY MONTH FOR A " \
             "YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$50 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:5,&quot;updated_at&quot;:1485563704," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006318?signature" \
             "=1516599830.7b657c42709c62f47ad5b8a890fae7f715a593c1&quot;}}},{&quot;id&quot;:1006321," \
             "&quot;minimum&quot;:60.0,&quot;reward&quot;:&quot;›››SIGNED SIGNATURE SNACK " \
             "PACKS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SURPRISE MAIL EVERY MONTH FOR A " \
             "YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››SIGNED SIGNATURE SNACK PACKS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SURPRISE " \
             "MAIL EVERY MONTH FOR A YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$60 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:2,&quot;updated_at&quot;:1492106062," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006321?signature" \
             "=1516599830.d69f4079af9551a69fabdeea8ae4385b4ae1e6df&quot;}}},{&quot;id&quot;:1006322," \
             "&quot;minimum&quot;:70.0,&quot;reward&quot;:&quot;›››LIVE 1 HOUR SYNTH CONCERT OVER SKYPE FOR YOU AND " \
             "YOUR FRIENDS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SIGNED SIGNATURE SNACK " \
             "PACKS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SURPRISE MAIL EVERY MONTH FOR A " \
             "YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;description&quot;:&quot;›››LIVE 1 HOUR SYNTH CONCERT OVER SKYPE FOR YOU AND YOUR " \
             "FRIENDS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SIGNED SIGNATURE SNACK " \
             "PACKS‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››SURPRISE MAIL EVERY MONTH FOR A " \
             "YEAR‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››I WILL DRAW YOU AND SEND YOU THE " \
             "DRAWING‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››!!!!!!!!!!!!ONE OF THE ORIGINAL DRAWINGS IN THE " \
             "BOOK!!!!!!!!!!!‹‹‹‹\\r\\n›››I WILL WRITE A PERSONALIZED POEM ABOUT ANYTHING FOR YOU‹\\r\\n›››2 LIMITED " \
             "EDITION 2 SIDED RADDDDD/SNCKPCK POSTERS‹‹‹‹\\r\\n›››15 ‘SNCKPCK’ STICKERS [NEW " \
             "DESIGN]‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››HAND WRITTEN LETTER‹‹‹‹‹‹‹‹‹\\r\\n›››2 SIGNED COPIES OF THE " \
             "BOOK &#39;RADDDDD&#39;‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹\\r\\n›››YOUR NAME IN THE BOOK AS A " \
             "SUPPORTER‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹‹ \\r\\n›››SECRET NOTE INSIDE‹‹‹‹‹‹‹‹‹‹‹‹‹&quot;," \
             "&quot;title_for_backing_tier&quot;:&quot;$70 reward&quot;,&quot;starts_at&quot;:0," \
             "&quot;ends_at&quot;:0,&quot;shipping_enabled&quot;:false,&quot;estimated_delivery_on&quot;:1351728000," \
             "&quot;project_id&quot;:718749111,&quot;backers_count&quot;:3,&quot;updated_at&quot;:1485547599," \
             "&quot;rewards_items&quot;:[],&quot;urls&quot;:{&quot;api&quot;:{" \
             "&quot;reward&quot;:&quot;https://api.kickstarter.com/v1/projects/718749111/rewards/1006322?signature" \
             "=1516599830.6c852cb1db7c20b7db35fc573dba69b033135ee2&quot;}}}],&quot;items&quot;:[]," \
             "&quot;livestreams&quot;:[]} "
    string2 = HTMLParser.HTMLParser().unescape(string)
    d = json.loads(string2)
    print d


