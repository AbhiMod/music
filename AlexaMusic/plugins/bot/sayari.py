from AlexaMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from config import BOT_USERNAME
spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
        ####
        
SHAYRI = [ " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
           " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**काश वो दिन जल्दी आए,जब तू मेरे साथ सात फेरो में बन्ध जाए।**🌺 \n\n**🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**महादेव ना कोई गाड़ी ना कोई बंगला चाहिए सलामत रहे मेरा प्यार बस यही दुआ चाहिए।**🌺 \n\n**🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**फिक्र तो होगी ना तुम्हारी इकलौती मोहब्बत हो तुम मेरी।**🌺 \n\n**🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**सुनो जानू आप सिर्फ किचन संभाल लेना आप को संभालने के लिए मैं हूं ना।**🌺 \n\n**🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**सौ बात की एक बात मुझे चाहिए बस तेरा साथ।**🌺 \n\n**🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**बहुत मुश्किलों से पाया हैं तुम्हें, अब खोना नहीं चाहते,कि तुम्हारे थे तुम्हारे हैं अब किसी और के होना नहीं चाहते।**🌺 \n\n**🥀Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**बेबी बातें तो रोज करते है चलो आज रोमांस करते है।**🌺 \n\n**🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**सुबह शाम तुझे याद करते है हम और क्या बताएं की तुमसे कितना प्यार करते है हम।**🌺 \n\n**🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**किसी से दिल लग जाने को मोहब्बत नहीं कहते जिसके बिना दिल न लगे उसे मोहब्बत कहते हैं।**🌺 \n\n**🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**मेरे दिल के लॉक की चाबी हो तुम क्या बताएं जान मेरे जीने की एकलौती वजह हो तुम।**🌺 \n\n**🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**हम आपकी हर चीज़ से प्यार कर लेंगे, आपकी हर बात पर ऐतबार कर लेंगे, बस एक बार कह दो कि तुम सिर्फ मेरे हो, हम ज़िन्दगी भर आपका इंतज़ार कर लेंगे।**🌺 \n\n**🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**मोहब्बत कभी स्पेशल लोगो से नहीं होती जिससे होती है वही स्पेशल बन जाता है।**🌺 \n\n**🥀Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.🥀\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}**",
           " 🌺**तू मेरी जान है इसमें कोई शक नहीं तेरे अलावा मुझ पर किसी और का हक़ नहीं।**🌺 \n\n**🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**पहली मोहब्बत मेरी हम जान न सके, प्यार क्या होता है हम पहचान न सके, हमने उन्हें दिल में बसा लिया इस कदर कि, जब चाहा उन्हें दिल से निकाल न सके।**🌺 \n\n**🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**देख के हमें वो सिर झुकाते हैं। बुला के महफिल में नजर चुराते हैं। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद आएगी.**🌺\n\n**🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**प्यार किया तो उनकी मोहब्बत नज़र आई दर्द हुआ तो पलके उनकी भर आई दो दिलों की धड़कन में एक बात नज़र आई दिल तो उनका धड़का पर आवाज़ इस दिल की आई.**🌺\n\n**🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**कई चेहरे लेकर लोग यहाँ जिया करते हैं हम तो बस एक ही चेहरे से प्यार करते हैं ना छुपाया करो तुम इस चेहरे को,क्योंकि हम इसे देख के ही जिया करते हैं.**🌺\n\n**🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺**सबके bf को अपनी gf से बात करके नींद आजाती है और मेरे वाले को मुझसे लड़े बिना नींद नहीं आती।**🌺\n\n**🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀**\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           " 🌺**सच्चा प्यार कहा किसी के नसीब में होता है. एसा प्यार कहा इस दुनिया में किसी को नसीब होता है.**🌺\n\n**🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀** \n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           " 🌺  प्यार तो करते नहीं तुम,\nदुआ करो मुझे कोई और पटा ले😂😂😁😁😜🙈🙈🙈😘😘❤️❤️❤️\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  वो ज़रा निगाहें तो उठायें , \n     कह दूं मैं प्यार का सलाम ...  \nऔर निगाहें झुकने से पहले ही ,\n         सरी उम्र लिख दूँ उनके नाम ... \n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",   
           "🌺  यह तो सोचा तुमने की तुम्हारे पीछे पड़े थे हम पर,\n   ये नहीं जाना की खुद से आगे माना हुआ था तुम्हें...💯🔥💔\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  ज़रा सी बिंदी ही तो लगा कर के वो निकलती है\n  सारे मुहल्ले में ये कोहराम सा क्यूँ मच जाता है ..\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}"  ,  
           "🌺  मुझे तो तुमसे नाराज़ होना भी नही आता न जाने तुमसे कितनी मोहब्बत कर बैठा हु मै  \n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",     
           "🌺  क्या करें जो दिल तुम पर आ गया\nतेरा मुस्कुराना बस हमें भा गया,\n\nबार बार तुझे देखने की चाहत हुई\nचेहरा तेरा हसीं ख्वाब दिखला गया,\n\nमोहब्बत तेरी में दिल धड़कने लगा\nआजाद परिंदा पिंजरे में समा गया,\n\nदीवाना, शौदाई  लोग हमें कहने लगे\nहर नाम लेकिन मेरे दिल को भा गया। ..\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  मोहब्बत कर देती है इंसान को खुदा।\nसजदे में फिर भी वो रहता है सदा।\n\nदिल धड़के किसी और के नाम पर\nजाने कैसे होता है हक ए इश्क अदा।\n\nजीते हैं नाम लेकर किसी और का\nअनदेखे एहसानो से रहे दिल लदा‌।।",
           "🌺  चाँद को अपनी निगाहों में उतारो तो सही ,\n    हम चले आयेंगे दिल से पुकारो तो सही ,\nदिल की दहलीज मोहब्बत से सजा रखी है ,\nथोड़ा सा वक़्त हमारे साथ गुजारो तो सही...❤️❤️❤️❤️\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  आओ जिंदगी\nभोकाल बनाए\nऔर अपुन दोनो मिलके \nसम सान में चाय \nबनाए 😁😁😁😁\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  सुनो..\n\nमुझे वो पोस्ट नही मिल रही 🙄🙄\nजिस पे सब फिदा हो जाएं 🤭🥰😂😂\nसूना आपलोग ने....\n😝😝😝🙈🙈😂😂🙈🙈\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  ★─●───❖──❖──❖───●─★\n\nजीवन में कभी कभी....\nहम बिना कुछ गलत किए भी बुरे 🥺 बन जाते है...! 💫\nक्योंकि लोग जैसा चाहते है...\nहम वैसे नही❌ बन पाते है...! 💫\n\n★─●───❖──❖──❖───●─★\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  श्री कृष्ण कहते है -\n    जो तुम्हारा साथ 🫴 दे तुम उसका साथ🤝 दो..!\nजो तुमको त्याग 💔 दे , तुम भी उसे त्याग❤️‍🔥 दो..!\n❣❣❣\n\n✍  ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  तुम हमे छोड गए… .\nइसमे तुम्हारा क्या कसुर… .\n\nहर कोई हमारा साथ… .\nनिभा भी नही सकता… .\n\n       ✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  बहुत तारीफ करता था मैं \nउसकी बिंदी की .\nलफ्ज़ कम पड़ गये जब \nउसने झुमके पहने\n\n🥰🥰🥰❤️❤️\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  तेरे कानों के झुमके\nतेरे माथे की बिंदी\nतेरे हाथों की मेहंदी \nतेरी आंखों का काजल \nतेरे प्यारे गाल\nतेरे लम्बे घने बाल\nतेरे होठों की लिपस्टिक\nतेरे पैरों की पायल\nतेरे होठों पे वो मेरा नाम...\n\nकितना कुछ कहना था मुझे....!!\n\n—————🖤🖤—————\n\n       ✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  ⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️\n\nपूरी धरा भी साथ दे\nतो और बात है...\n\nतु ज़रा भी साथ दे\nतो और बात है....!!\n—————🖤🖤—————\n\n⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️\n\nᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  दोस्तों....✍\n\nकोशिश करना वो शख्स आपको हमेशा मुस्कराता हुआ मिले...😊\nजो रोज आपको आईने में दिखाई देता है !! 🥰\n\nᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟\n\nएक दम से मिलते हैं\nएक दम से खो जाते हैं...\nलोग जो बनते हैं कभी हमारी जरूरत\nज़रुरत के वक्त पराए हो जाते हैं...!!\n—————🖤🖤—————\n\n🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄\n\n      ✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  पता नहीं मुझें क्या हो\nगया है😔😒\n\nशीशा भी देखू तो \n   खुद का ही\nचेहरा नज़र आ रहा है।\n    कही मुझे प्यार तो नही हो गया 🙈😜🥴\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  आज मेरे घर वालो ने मेरा.\n Whatsaap 😔 check किया...\n\nउन्हें क्या पता मै सारे कांड\nTelegram ✔️ पर करता हूँ..\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @AM_YTBOTT",
           "🌺  जो चीज सेल और बेट्री दोनो से चले\n    उसे सेलिब्रिटी कहते हैं😄\nहाय रे मेरा नॉलेज 🙈😂😂😝😝\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME} ",
           "🌺  एक तेरे चेहरे से दिल लगा बैठी मेरी ये आंखे।।।\n\nऔर कोई नजर आता नहीं इस जहा में तेरी\nखूबसूरत अदाओं के आगे ।।।\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺  रिश्ते जितने सुंदर होते हैं,\nदर्द भी उतने ही गहरे होते हैं.\nकोई देखता नहीं वो आंखे,\nजिनमे समन्दर ठहरे होते हैं.....\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "🌺 .न मुहब्बत ,न दोस्ती ..,\n     हमे कुछ रास नहीं ।\nसब बदल जाते हैं …..।।\n  हमारे दिल में जगह बनाने के बाद ।।💔💔\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           "Hello welcome to our group ✨🌎\n\nAll languages are allowed ✅🔥\n\nFeel free to express yourself \n\nWe don't ban/mute our members without reason 🔥💬\n\n24/7 active with best users \n\nEasily to be friend with them🫂💜\n\nPlease join us 👇\n https://t.me/+jCS-YsVBVEE3NjQ1\nhttps://t.me/+jCS-YsVBVEE3NjQ1\nhttps://t.me/+jCS-YsVBVEE3NjQ1\nhttps://t.me/+jCS-YsVBVEE3NjQ1 \n\n\n✍ ᴡʀɪᴛᴛᴇɴ ʙʏ : @{BOT_USERNAME}",
           ]
          

# Command
    


@app.on_message(filters.command(["shayari","sari","sayari","sayri"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/shayaril  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["no"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ OFFFFFFFFF♦")
