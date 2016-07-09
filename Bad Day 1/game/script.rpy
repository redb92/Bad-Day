# Declare images below this line, using the image statement.
image bg bedroom = "bg bedroom.jpg"
image bg blackscreen = "bg blackscreen.jpg"
image bg bedroom2 = "bg bedroom2.jpe"
image bg street1 = "bg street.jpe"
image bg street2 = "bg street.jpe"
image bg building outside = "bg street.jpe"
image bg bus station = "bg bus station.jpe"
image bg living room = "bg living room.jpe"
image carol happy = "carol happy.png"
image carol smile = "carol smile.png"
image carol neutral = "carol neutral.png"
image carol concerned = "carol troubled.png"
image carol angry = "carol angry.png"
image carol blush = "carol blush.png"

# Declare characters used by this game.
define c = Character('Carol', color="#b45f04")
define a = Character('Alan', color="#5858fa")
define j = Character ('Julian', color="#04B404")
define k = Character ('Katherine', color="#FF0040")
define s1 = Character ('Stranger 1', color="#8904B1")
define s2 = Character ('Stranger 2', color="#8904B1")

define dissolve = Dissolve (.5)

# The game starts here.
label start:
    
    scene bg blackscreen with dissolve
    
    pause 2

    centered "Is it realistic to feel like I’m special to others?"

    centered "Is it realistic to think I can make a difference in a friend’s life, that I can help them out in their times of need?"
    
    centered "Is it realistic to hope they’ll lean on my shoulder and call my name when things get tough?"
    
    pause 1
    
    c "I tried to kill myself last summer."
    
    pause 2
    
    centered "That day, for the first time, I began to doubt it was."
    
    pause 1
    
    scene bg bedroom with Dissolve (2)
    pause 1
    play music "scene 1.mp3"
    pause 2.5 
    
    "Autumn had only just begun, but leaves were already falling off their branches."
    
    "Sitting at opposite sides of a small table, me and Carol, whom I hadn’t seen for a while, chatted as usual."
    
    "It’s puzzling, because that’s the only thing I can remember from that day."
    
    "I can’t remember what made her bring it up, or if there were any special circumstances surrounding our meeting."
    
    "I only know that at some point she said it:"

    show carol neutral with dissolve
    pause .75
    
    c "I tried to kill myself last summer."
    
    "How was I supposed to respond?"
    
    "Bewildered, I remained silent, giving Carol the time to continue."
    
    show carol happy
    
    c "You look surprised."
    
    "She sounded nervous."
    
    c "I don’t blame you: I can’t believe it myself either."
    
    show carol neutral
    
    c "It’s a bit hard to explain..."
    
    "Carol took a deep breath."
    
    c "That night, I suddenly felt the urge to take some pills, any pills I could find, and then shove them down my throat, as if nothing else mattered."

    c "I don't know what gave me the idea."
    
    c "Maybe I saw them there, in the corner of my eye..."
    
    c "I only know that I did it."
    
    c "...and it was weird."
    
    c "I hallucinated for the first time in my life."
    
    show carol happy
    
    c "Some of it was scary, but some of it kinda exciting as well."
    
    show carol smile
    
    c "Looking back on it, I might've even had fun!"
    
    "I felt the urge to interrupt, but I restrained myself, reluctantly."
    
    show carol happy
    
    c "The next morning I woke up in a hospital, dizzy, unable to remember most of what happened the other night."
    
    c "I told my parents what I had done..."
    
    show carol troubled with dissolve
    
    c "...and as expected, they didn’t take it too well."
    
    c "The doctors advised me to rest, but that I’d be able to leave soon, because the pills hadn’t done anything weird to my body."
    
    show carol happy
    
    c "...guess I should’ve gone with a shotgun instead, huh?"
    
    show carol smile with dissolve
    pause 1.5
    show carol troubled with dissolve
    pause 1.5
    
    "She tried to laugh again, but stopped after looking at my face."
    
    c "...I got discharged a few days after."
    
    show carol happy
    
    c "Things went back to normal pretty quick: I visited my cousins, spent some days at the beach, had some fun with Julian and his friends…"
    
    show carol neutral
       
    c "But when the time came for me to come back, my parents refused to let me go."
    
    show carol troubled
    
    c "It wasn’t hard for me to see why. Their only daughter had just tried to kill herself, so of course they’d react the way they did."
    
    c "“Why can’t you attend a school from around here?“ they asked."
    
    show carol neutral
    
    c "In the end, I promised to visit a psychiatrist at least once a week, to give them some peace of mind."
    
    show carol angry
    
    c "It doesn’t stop them from calling every day to check if I’m still at it."
    
    a "Are you?"
    
    show carol happy
    
    c "Yes."
    
    c "It sucks, but I am."
    
    c "I’m also on pills."
    
    c "That’s really all what going to the doctor is good for: pills, pills, loads of pills, so that I never feel like killing myself again."
    
    c "It’s all pretty ironic when you think about it."
    
    a "..."
    
    "I couldn’t bring myself to smile."
    
    c "And that's all there is, Alan."
    
    a "Everything?"
    
    c "Yup. I've summed it up as best as I could."
    
    show carol concerned
    
    c "Don’t tell a soul, alright?"
    
    c "Not a lot of people know about this... and I want it to remain that way."
    
    a "I give you my word."
    
    a "Who else have you told?"
    
    show carol neutral    
    
    c "My family, Julian, a couple of friends from back home… that’s about it."
    
    "It wasn’t something that you would tell just anyone."
    
    "Keeping it among close friends and family was the most logical thing to do."
    
    "It made sense… but if she hadn’t chosen to tell me that day, would I have known about it eventually?"
    
    "Or would I have been kept in the dark, blissfully unaware of Carol's suffering?"
    
    "“Why did you do it?“ I wanted to ask. But the words got caught up in my throat, they refused to let go; they were afraid she might've not responded, proving that I wasn’t trustworthy enough in her eyes."
    
    show carol troubled with dissolve
    
    c "I’m not sure why I did it."
    
    "But she tried to answer anyways."
    
    c "I’ve got good grades, right? And Julian is still by my side."
    
    c "Honestly, there wasn’t anything wrong with my life."
    
    c "But that morning, when I looked myself in the mirror, I just felt…"
    
    c "It was all just so…"
    
    c "..."
    
    show carol happy
    
    c "…no, you don’t want to hear it."
    
    "But I did."
    
    "So I really should've said..."
    
    jump return1
    label return1:
    
    menu:
        "“Please tell me.“":
            jump return1
        
        "“You probably don't want to talk about it.“":
            jump choice1
            
    label choice1:
        
    a "You probably don’t want to talk about it."
    
    "Don’t say that, Alan."
    
    c "No… I really don’t."
    
    "Don’t let her say that, Alan."
    
    a "Then that’s alright. I’ve heard enough."
    
    "“Tell me once you feel ready“."
    
    "...I forgot to add."
    
    show carol smile
    
    c "Yeah, thanks for putting up with me!"
    
    a "Don’t worry about it. We’re friends after all. Gotta look out for each other."
    
    show carol happy    
    
    c "Damn right!"
    
    c "And don’t worry: I’m not planning to do it again. It was, you know, just a bad day."
    
    c "For no reason at all, I woke up feeling like it was the worst day ever…"
    
    c "We all have mornings like that, right?"
    
    hide carol smile with dissolve
    pause 1.5
    
    "It was a clear day, just like every other early autumn day."
    
    "We chatted in her living room, just like every Friday afternoon."
    
    "Every Friday, because it was only on Fridays that neither of us had classes to attend."
    
    "In her living room, because we were neighbors, and her place was always tidier than mine."
    
    "Every day we’d wake up at roughly the same time, eat breakfast, and then step out of our apartments to meet in the corridor outside."
    
    "We’d walk the 20 minutes that separated us from the local college, making small talk on the way, going our separate ways upon reaching the main gates."
    
    "Two years, always the same routine."
    
    "I had gotten used to her, and she had gotten used to me. It was only natural that our incidental friendship would grow into something else."
    
    "By that, I don't mean anything romantic."
    
    show carol happy with dissolve
    
    a "Is Julian home?"
    
    c "He’s at the conservatory, practicing for his next audition."
    
    a "It must be hard to make it as a musician."
    
    c "There are a lot of talented people there… but he still has a chance."
    
    show carol smile
    
    c "He’s a genius after all!"
    
    a "I’ll take anything you say with a grain of salt. I wish him the best though."
    
    show carol angry
    
    c "What’s that supposed to mean…?"
    
    "Julian was Carol’s boyfriend."
    
    "A nice fellow, though we never talked much. He was a violinist trying his best to survive in the ruthless world of classical music."
    
    "Carol and Julian had known each other since they were little, and started dating while still in high school."
    
    "They decided to move in together to the big city a year after graduating, as education back in their hometown just wasn’t enough for their grander goals."
    
    a "Really, you just can’t make a living out of music, or any type of art, for that matter."
    
    c "Hmph, now you’re just being an asshole!"
    
    "Incidentally, Carol was a writer; a struggling poet of sorts."
    
    show carol happy
    
    c "I’ll get a book published one day, just you see."
    
    a "Sure, break a leg."
    
    show carol neutral
    
    c "...Take me seriously, alright?"
    
    c "You know it's something important to me."
    
    a "...Alright. You have my support."
    
    a "I mean it."
    
    show carol troubled
    
    "But she didn’t take my word for it and just looked away."
    
    "I knew she was faking her anger for the most part, but still, it made me regret my words."
    
    "I considered my options, wondering what would be the best way to cheer her up."
    
    a "Wanna go eat some donuts?"
    
    c "..."
    
    a "How about a public reading? You like those, don’t you?"
    
    c "..."
    
    a "..."
    
    hide carol troubled with dissolve
    
    "Despite my best efforts, I wasn’t getting anywhere."
    
    "I looked around the room, searching for something that could help me break the awkwardness."
    
    a "…t-this place is awfully messy today."
    
    show carol angry with dissolve
    
    c "I know, right?!"
    
    "Carol suddenly jumped up from her seat."
    
    c "Julian just threw his clothes everywhere and left a huge-ass mess on the kitchen last night! And I’ve barely had any time to clean!"
    
    c "Why should I clean anyway? It’s his mess, so HE should be the one to clean!"
    
    a "Sounds fair."
    
    c "Also, last night, after cooking? He just went to sleep, without even giving me a kiss! I feel unloved, man."
    
    c "Plus I was finally in the mood for some-"
    
    pause 1.5
    
    "She putted a stop to her words."
    
    a "I understand. Still, he was probably tired, that's all."
    
    c "Yeah, I know he was tired! He’s always tired! It’s the worst!"
    
    c "And I gotta be here, and clean after him, and with school and all it’s just too much!"
    
    c "..."
    
    show carol happy
    
    c "Well, I suppose I can make him apologize later tonight."
     
    "Getting her to complain about Julian was always a good way to lift her spirits."
    
    "As with every relationship, theirs had its ups and downs, but I knew that deep down they loved each other: she was always going to put up with his mess, and he was always going to put up with her complaints."
    
    "I was jealous, in more than one way."
    
    hide carol happy with dissolve
    pause 1.5
    
    "…and that’s how it usually went."
    
    "We talked: about our lives, about the people in our lives, about the lives of the people in our lives."
    
    "It was a Friday afternoon just like always, except…"
    
    scene bg blackscreen with dissolve

    c "“I tried to kill myself.“"
    
    scene bg bedroom with dissolve
    
    "I’m sure she didn’t want me to dwell on it; I’m sure she wanted me to act like always, to not let it weigh on my soul."
    
    scene bg blackscreen with dissolve
    
    c "“I tried to kill myself last summer.“"
    
    scene bg bedroom with dissolve
    
    "But I couldn't."
    
    "I couldn't get that out of my head."
    
    "Whenever I thought back on it, whenever I tried to find an explanation, my heart just fell into a spiral of confusion and contempt."
    
    "Carol was one of the brightest people I ever had the luck to meet."
    
    "She greeted the day with a smile, she worked with a smile, and whenever things got tough, she brushed it off tried her best to overcome it."
    
    "I just couldn’t imagine her with dozens of pills down her throat."
    
    "I couldn’t imagine her with the drive to end her own life."
    
    "But she did, she told me so. Unless she was lying... which made no sense."
    
    "I couldn’t understand her, and that bothered me."
    
    "That she never shared any of her problems with me bothered me even more."

    scene bg blackscreen with dissolve
    pause 1.5
    
    "However, the absolute worst part was how, for roughly 3 months, I never knew about any of this happening."
    
    "How she never called me, not even to say hi, during the entirety of that summer."
    
    scene bg bedroom with dissolve
    show carol happy with dissolve
    pause 1
    
    c "Something wrong, Alan?"
    
    a "…no."
       
    a "Nothing’s wrong."
    
    "I lied, shamelessly."
    
    hide carol happy with dissolve
    scene bg blackscreen with Dissolve (1)
    stop music fadeout 1
    pause 3
    
    "That conversation with Carol occupied my mind for the next couple of weeks."
    
    "I was worried, but trying to fix an unsolvable problem wasn’t going to be of any use, so I composed myself as best as I could."
    
    scene bg bedroom2 with dissolve
    pause 1
    
    "Besides, I had my own issues to deal with."
    
    "Dating is a complicated thing, after all."
    
    pause 1
    play sound "cell vibrate.wav"
    pause 2
    queue sound "cell vibrate.wav"
    pause 3
    
    k "Hey."
    
    a "Hey."
    
    k "..."
    
    k "Umm, so, it might be a bit sudden, but..."
    
    k "I think we should break up."
    
    "It all came falling down on me with a single phone call from my then-girlfriend, Katherine."
    
    "As I let those words sink in, I realized they didn’t hurt as much as I thought they would."
    
    a "...alright."
    
    a "I understand."
    
    k "..."
    
    a "..."
    
    a "Kate?"
    
    k "Is that all you’re going to say?"
    
    "My complacency must’ve rubbed her the wrong way."
    
    a "No, I had been giving the idea some thought as well."
    
    a "We barely see each other nowadays: I’m busy studying, you’re busy with your job, and besides…"
    
    k "…we’re not as into it as we used to be, right?"
    
    a "You read my mind."
    
    "She sighed, possibly in relief."
    
    k "Honestly, I’m glad you feel the same way."
    
    "Of course, I had no way of knowing if she was telling the truth."
    
    a "Like this, no one gets hurt."
    
    k "Yeah…"
    
    k "No one gets hurt..."
    
    "There was another long, awkward silence."
    
    k "So this is goodbye."
    
    a "Why?"
    
    a "We might not be lovers anymore, but we can still meet up every now and then to chat, maybe even have a drink."
    
    a "It’s still possible to be friends."
    
    k "...yeah."
    
    "She giggled on the other side."
    
    k "Yeah, it is."
    
    "I was fully aware it wasn’t possible: any and all meetings between us were going to be awkward from then on."
    
    "My only intent was to ease the tension, make her laugh for one last time."
    
    k "Later then."
    
    a "Yeah, later."
    
    pause 2
    
    "Kate hung up."
    
    "Just like that, a relationship of eight months came to an end."
    
    pause 1
    play music "scene 2.mp3"
    pause 2.5
    
    a "It's finally over, huh..."
    
    "I contemplated the screen of my phone in a daze, all while thinking about my time spent with Kate."
    
    "If someone were to ask me if being with her made me unhappy, I’d say not really."
    
    "It simply didn’t make me happy enough."
    
    "At some point, we became more friends than lovers, and then simply casual friends that were too scared of hurting each other to break up."
    
    "Kate was brave enough to take that final step."
    
    "I wasn’t."
    
    "Somewhere inside, I was jealous of her bravery."
    
    "Still, eight months… that’s a long time. Enough time to get attached to someone."
    
    "I wondered if she was truly alright with breaking up." 
    
    "I wondered if she didn’t do it just to make things easier on me."
    
    "It was something I couldn’t ask, something that I’d never know."
    
    play sound "cell vibrate.wav"
    pause 2
    queue sound "cell vibrate.wav"
    pause 2    
    
    "My phone rang again. Was it Kate?"
    
    a "..."
    
    "No, it was Carol."
    
    "I quickly picked it up."
    
    pause 2
        
    c "Hey buddy!"
    
    c "Do you have any time to spare?"
    
    a "Do YOU have any time to spare? Aren’t you supposed to be in class now?"
    
    c "Listen to this! Our teacher didn’t show up, and he didn’t even send an email to warn us!"
    
    c "So I’m at home now, watching some TV."
    
    c "Wanna go have a drink with an old friend?"
    
    a "…Nah, I'm not really feeling it."
    
    c "Why? What’s wrong?"
    
    a "I just broke up with Kate… so you know, not a great time."
    
    stop music fadeout 2
    pause 1.5
    
    c "..."
    
    pause 2
    
    "Carol hung up the phone."
    
    pause 1.25
    
    play sound "knocking door.wav"
    pause 2
    
    "Moments later, a pair of fists furiously knocked against my door."
    
    scene bg blackscreen with dissolve
    
    "Slowly, methodically, I unlocked the door to let Carol in."
    
    play sound "unlock door.wav"
    pause 2.2
    
    show carol angry with moveinleft
    
    c "What?! Why?! How?!"
    
    c "Just what did you do, Alan?!"
    
    a "Calm down. I didn’t do anything."
    
    c "But you looked so cute together! And she was such a sweet girl! Just why would…?!"
    
    "She was so out of breath that she couldn’t even finish her words."
    
    a "Alright, I get it! Just sit down, ok?"
    
    a "I’ll go get you some water."
    
    hide carol angry with dissolve
    scene bg bedroom2 with dissolve
    pause 1
    play music "scene 2.mp3"
    pause 2
    
    "A minute later we walked into my room, and Carol thankfully got a grip on herself by then."
    
    show carol angry with dissolve
    
    c "So? Please explain."

    "I tried to explain myself: how I didn’t feel particularly happy being in a relationship, how we barely had time to see each other, how in the end Kate ceased to feel like a lover."
    
    show carol neutral    
    
    "Carol listened to me in silence, nodding every once in awhile."
    
    c "I see."
    
    show carol happy
       
    c "Well, if that’s how it was, then it’s only logical to break up… but it feels like a waste."
    
    a "How so?"
    
    c "You looked good together, and you seemed to understand each other very well."
    
    show carol smile
    
    c "I kinda hoped to see you guys getting married one day."
        
    "Her words perplexed me."
    
    show carol happy    
    
    "Me? Married with Kate?"
    
    "I tried to picture the scene, she and I sharing a home, raising a family, living as husband and wife."
    
    "...but it felt too surreal to imagine."
    
    a "The thought never crossed my mind."
    
    show carol concerned
    
    c "Really? Not even once?"
    
    a "No. Or at least, not that I remember."
    
    show carol neutral
       
    a "Maybe I imagined it once, back when we first started, but now it feels so distant that I can’t be sure."
    
    show carol concerned
    
    c "That’s a bummer."
    
    hide carol concerned with dissolve
    
    "Carol sat on my bed and leaned back on the cushions."
    
    show carol happy with dissolve
    
    c "It must’ve been my imagination then."
       
    c "You guys liked the same things, attended the same classes, rarely ever had a fight..."
    
    show carol angry
                                                                                                        
    c "I never heard you complain about her, and she CERTAINLY never complained to me about you."
    
    a "Well, it just comes to show things aren’t always as good as they-"
    
    a "..."
    
    "But something caught my ear."
    
    a "Wait, Carol."
    
    a "You talked with Kate a lot?"
    
    show carol happy    
    
    c "Yeah! Once a week, I guess."
    
    "That was a legitimate surprise."
    
    a "…I didn’t know you were that close. I thought you only saw each other when she visited me."
    
    c "It used to be that way, but she added me on Facebook a few months ago and we’ve been hitting it off ever since."
    
    a "I see. I wasn’t expecting that."
    
    c "In fact, she told me quite a few things I didn’t know about you. Wanna know what?"
    
    a "...no, I really don’t want to ask."
    
    show carol smile
    
    c "Wise choice!"
    
    "I took a deep breath."
    
    show carol happy
    
    a "As I was saying, things aren’t always as good as they seem."
    
    c "How so?"
    
    a "We never had a fight, true, but that’s not necessarily a good thing."
    
    a "It’s not that we didn’t fight because we liked everything about each other."
    
    a "No, that’s impossible."
    
    show carol neutral
    
    a "We just did our best to avoid conflict… and thanks to that, we never expressed our dissatisfaction, and our relationship never grew as a result."
    
    "Thinking back on it, holding back any and all complaints was probably our biggest mistake."
    
    c "I suppose you two were never truly in love then."
    
    a "You’re probably right."
    
    show carol concerned
    
    c "Ahh, damn… but you looked so good together."
    
    c "Such a waste… such a waste…"
    
    hide carol concerned with Dissolve (1)
    
    "Carol mumbled the same thing over and over, but she eventually stopped to set her gaze across the window."
    
    "It was a gray day outside. Dark clouds covered the sky, threatening to fill the entirety of this town with endless rain."
    
    "Had I ever truly fallen in love with someone until then?"
    
    "I tried to look back to my elementary school days, to my high school days, up to the current date, but I could only remember one time when I was truly “in love“."
    
    show carol happy with dissolve
    
    a "You know… back when we first started hanging out? I was kinda in love with you."
    
    stop music fadeout 1
    
    c "..."
    
    c "Eh?"
    
    a "Back when we were freshmen I was in love with you."
    
    a "Like, seriously in love."
    
    "For a moment, Carol became unable to respond, my sudden confession overwhelming all of her senses."
    
    show carol blush with dissolve
    
    "Little by little her cheeks took a reddish color, and so did her ears."
    
    "She tried to say something, anything, but nothing came out of her mouth."
    
    a "...are you ok?"
    
    pause 3
    
    show carol happy
    
    c "Y-yeah, of course I’m okay."
    
    c "But damn..."
    
    show carol smile
    
    c "You really don’t know how to pull your punches, huh?"
    
    hide carol smile with dissolve
    
    play music "scene 2.mp3"
    pause 1.2
    
    "She tried to brush it off, but she was clearly a bit shaken, or dare I say, confused: Carol never expected me to hold such feelings for her; she never thought I’d see her in such a special light."
    
    "It was sad, somehow."
    
    "Admitting my past feelings for her didn’t make me uncomfortable."
    
    "They were “past feelings” for a reason: any passion I ever felt towards the idea of dating Carol had faded long ago."
    
    "Now she was just a friend, and my only wish was for our relationship to remain that way."
    
    "However, her reaction, her expression… I didn’t like it."
    
    "It made me fear she might have taken my words far more seriously than she should’ve."
    
    "I just wanted to tease her back, but maybe it was a mistake? Maybe I should’ve kept my mouth shut?"
    
    show carol happy with dissolve
    
    "She was still looking at me… as if trying to discern my thoughts."
    
    "I looked away with a bunch of conflicted feelings climbing up my back."
    
    c "What was it that you liked about me?"
    
    "She spitted out a question I didn’t want to answer."
    
    a "It was too long ago, so I can’t remember."
    
    show carol angry
    
    c "Can’t you make an effort?"
    
    "Carol wouldn’t drop it. She moved closer, enough to make me crawl back on my seat."
    
    "My words weren’t supposed to hold any special meaning, so why was she acting like that? What did she want?"
    
    a "..."
    
    show carol neutral
    
    c "Alan?"
    
    "She was pressing me for an answer."
    
    "What should I have said?"
    
    jump return2
    
    label return2:
    
    menu:
        "“What I liked about you was...“":
            jump return2
        
        "“It doesn't really matter...“":
            jump choice2
            
    label choice2:
    
    a "It doesn’t really matter, does it? It was more than a year ago, before I knew you had a boyfriend."
    
    show carol happy
    
    c "Then, hypothetically, if I hadn’t been with Julian at the time, what would you have done?"
    
    a "I don’t get what you mean."
    
    c "If I had been single, if I had been open to dating other people, would you have taken the chance?"
    
    "Annoying."
    
    "Troublesome."
    
    "Irritating."
    
    "It felt like it was an important matter to her, I could see it in her eyes, but it wasn’t a good idea to pursue it any further."
    
    a "Drop it. I’m not going to answer."
    
    show carol angry
    
    c "You’re the one who brought it up!"
    
    a "It’s not going to change anything."
    
    show carol happy
    
    c "Isn’t that more of a reason to answer?"
    
    a "Don’t twist my words to your advantage."
    
    show carol smile
    
    c "What’s the deal, Alan? We’re not going to stop being friends over something like this."
    
    c "It’s all in the past, right?"
    
    "And somehow, that’s enough to make me lose what little patience I was holding."
    
    stop music fadeout 1
    
    a "Would you just stop it already?!"
    
    show carol concerned with dissolve
    
    pause 1.5
    
    "I stood up from my seat. I didn’t walk up to her, I didn’t even look at her, I just stood up, enough to emphasize my growing anger."
    
    "A heavy silence engulfed the room."
    
    c "..."
    
    a "..."
    
    "I should’ve apologized then, but my mind wasn’t composed enough to do it."
    
    "Or rather, I didn’t want to do it."
    
    pause 2
    
    "Neither of us spoke for what felt like hours."
    
    pause 2
    
    show carol neutral
    
    c "I’m sorry. I shouldn’t have given you the chance to talk."
    
    "Her voice sounded hoarse."
    
    show carol concerned
    
    c "You have every right to be angry. Like, you broke up with your girlfriend just a second ago, so of course you’re angry!"
   
    show carol happy
   
    c "Really, just how self-centered can I get?"
    
    "Every word she said filled me with guilt."
    
    show carol smile
    
    c "I-I know! Wanna eat something? Drink? Maybe… watch a movie?"
    
    c "..."
    
    show carol neutral
    
    c "…Alan?"
    
    "But other than looking up, I said nothing in response."
    
    show carol happy
    
    c "…ok, you’re not in the mood. I understand."
       
    c "Then, do you need anything? Do you want to be left alone?"
    
    a "..."
    
    c "Gotcha, left alone it is."
    
    c "I’ll step out for the time being then, but call me if you need anything, alright? Promise me."
    
    a "…yeah, yeah, I promise."
    
    show carol smile
    
    c "Good boy!"
    
    hide carol smile with dissolve
    
    "She probably couldn’t understand the reason behind my anger."
    
    "It’d be unfair to hope she could, considering I myself had no idea."
    
    a "Let me see you out."
    
    show carol happy with dissolve
    
    c "You don’t need to. Or what? You think I’ll get lost?"
    
    a "Don’t be stupid."
    
    show carol smile
    
    "Carol laughed, but her voice was still a bit tense."
    
    show carol happy
    
    c "Well then… see you later."
    
    a "Wait..."
    
    hide carol happy with dissolve
    
    "“I’m sorry“. Was that the right thing to say?"
    
    "“It’s not your fault“. Was that the right thing to say?"
    
    "“Let’s forget we ever talked about this“. Was that the right thing to say?"
    
    a "I don’t remember what I liked about you..."
    
    "I lied, but Carol stopped in her tracks; I had her full attention."
    
    a "I really don’t remember… but you never seem to let anything ruin your mood, and you always seem… “bright”, if that’s the right word to use."
    
    a "I do admire you for that."
    
    "Carol remained by the doorway, her fingers pushed against the knob. She contemplated what to say in response."
    
    show carol concerned with dissolve
    
    c "Yeah..."
    
    pause 1.7
    hide carol concerned with dissolve
    show carol smile with dissolve
    
    c "Thanks."
    
    hide carol smile with dissolve
    play sound "door close.wav"
    
    pause 2.5
    
    scene bg street1 with dissolve
    
    pause 2
    
    "Needing some time to cool off, I decided to take a walk across the neighboring shopping district."
    
    "As I was trying to relax, I glanced at a peculiar sight."
    
    "A block away from me, in front of a trendy café, I recognized Carol talking with two other guys I didn’t know."
    
    a "...classmates, maybe?"
    
    "It was a rare occurrence to meet Carol outside our school campus, let alone see her in this part of town."
    
    "As friendly as she may have been, her days consisted mostly of going back and forth between her apartment and school."
    
    "Honestly, it never felt like she liked people too much, but I assumed it was only my imagination."
    
    "A large crowd separated us and I could barely keep her in my sight."
    
    pause 2
    
    "Little by little I tried to make my way across the street, careful not to run into anybody along the way."
    
    pause 2
    
    "As I got closer, however, I realized something was wrong with Carol and the two young men."
    
    "It was difficult to distinguish from where I stood, but they seemed to be, if not fighting, at least having a heated argument."
    
    c "C'mon, stop being so stubborn!"
    
    s1 "Right back at you. If you keep this up then we'll never decide on the order in time."
    
    c "I know, but..."
    
    s1 "You're not the only one who cares about the anthology. Please remember that."
    
    "The stranger was reaching the end of his patience."
    
    "His partner (or assumed partner) stood a few feet away, unwilling to join the conversation."
    
    "It didn’t look good. Carol kept arguing, oblivious to how the stranger’s expression was gradually getting more and more tense with each passing second."
    
    "Seeing no other choice, I prepared myself to step in."
    
    show carol angry at right with dissolve
    pause 1
    
    a "Yo, Carol! Fancy meeting you here!"
    
    "The three of them looked in my direction, and I tried my best to keep it cool."
    
    a "Is there a problem?"
    
    s1 "...who are you?"
    
    a "My name’s Alan. I’m Carol’s friend."
    
    show carol concerned at right
    
    "For a moment, the young man looked troubled by my appearance, but also a bit curious: he inspected me from top to bottom, as if trying to recognize me from somewhere."
    
    s1 "Are you a writer as well?"
    
    a "No, just a normal student."
    
    s1 "What do you study?"
    
    a "Economics."
    
    show carol neutral at right
    
    "The stranger looked me straight in the eye, but lost all interest shortly afterwards. It was only then that his partner decided to intervene."
    
    s2 "Let’s go man, we can keep talking about this next week. Is that ok with you?"
    
    show carol angry at right
    
    "He asked Carol, who I noticed was making a considerable effort to keep her mouth shut."
    
    c "...yeah, whatever. Next week is fine."
    
    "The two bid their farewells and left us on our own."
    
    show carol angry at center
    with move
    
    a "..."
    
    c "..."
    
    "Carol’s expression looked sour, and I was afraid of asking for a reason."
    
    pause 1
    
    show carol happy with dissolve
    
    pause 1
    
    play music "scene 3.mp3"
    pause 1
    
    c "Thanks for helping me out."
    
    c "A few more seconds and I would’ve exploded on the guy."
    
    a "Yeah, seems I was right on time. Who were they?"
    
    show carol neutral
    
    c "Just some people from my writing workshop, aspiring poets and all that jazz."
    
    "I couldn’t remember her ever mentioning going to a writing workshop, but I kept that to myself."
    
    a "Are they any good?"
    
    c "The aggressive one is pretty bad, but the other shows promise. It’s too early to tell though."
    
    a "Look at you, talking like some literary expert."
    
    show carol happy
    
    c "Hey, I’m better than the bunch of them, so I have a right!"
    
    c "..."
    
    show carol concerned
    
    c "Well, maybe I’m exaggerating a bit..."
    
    "She sighed, clearly lacking in her usual motivation."
    
    show carol neutral
    
    c "What are you doing here, Alan?"
    
    a "Nothing. Just walking around."
    
    a "...wanna come with me?"
    
    show carol happy
    
    c "Sure. A walk sounds fine."
    
    c "I need to vent somehow."
    
    hide carol happy with dissolve
    
    scene bg blackscreen with dissolve
    pause 2
    scene bg street2 with dissolve

    
    "We walked side by side for a couple of blocks."
    
    "The street went on before our eyes, with stores of all kinds exhibiting their products and illuminating the lane with all sorts of extravagant advertisements."
    
    "Long ago, Carol had explained to me how she disliked the city landscape, and how she preferred the quiet, humid forests and ever-raining skies of her home region to the incessant presence of skyscrapers over the horizon."
    
    "Whenever she was in a good mood she’d talk about the flowers that flourished in her garden, the beautiful river that split her town in half, the mysterious essence of nature that hadn’t yet been touched by the hands of “civilized” men."
    
    a "Why don’t you go back, then?"
    
    "Her response was:"
    
    show carol happy with dissolve
    
    c "This is the only place I can make it as a writer."
    
    hide carol happy with dissolve
    
    "It was a delicate issue to her, and I decided not to pry any further."
    
    "For two years, all I had ever known about her goals was that she wanted to be a writer, and not just “a writer”, but one of the greatest writers of this nation."
    
    "I didn’t know how writing worked, and I still don’t."
    
    "I didn’t know what writers needed to do in order to become great."
    
    "I had read some of her stuff, but I had never been able to understand it."
    
    "Metaphors were too foreign to the simple words and meanings I was used to."
    
    "Of course, even if we didn’t understand each other, we were still friends."
    
    "Friends don’t need to have dreams in common, or anything in common, to get along."
    
    "However, from time to time, I felt knowing so little about Carol, Carol as a writer, was a mistake."
    
    "That I should’ve tried to understand her better, or else our lives would have eventually drifted away."
    
    "Such thoughts scared the crap out of me."
    
    a "Do you not get along with those guys?"
    
    "I decided to ask after a few minutes of silence."
    
    show carol neutral with dissolve
    
    c "...not really."
    
    c "Oh, but I don’t hate them or anything! I just don’t... “like” them either. They are OK people, just not people I’d be friends with."
    
    show carol happy
    
    c "Does that make any sense?"
    
    a "It makes perfect sense. But if that’s the case..."
    
    c "You want to know why we were fighting, right?"
    
    c "It's so easy to tell."
    
    show carol smile
    
    c "C’mon Alan, we’re buddies, right?"
       
    c "You should ask whenever you feel like asking, otherwise you’ll hurt my feelings."
    
    a "...Alright then. Why were you fighting?"
    
    show carol happy
    
    c "Pride, mostly. Artists are prideful people: we’ll butt heads whenever someone talks shit about our work."
    
    show carol angry
    
    c "You see, the writing workshop I go to is “harsh”."
    
    c "Every week, our teacher asks us to hand over everything we’ve written over the past few days, be them short stories or poems, regardless of whether we’ve finished them or not."
    
    show carol happy
    
    c "We take turns to read our writing out loud, and then everyone shares their opinion on the text."
    
    c "Some might say it was good, some might say it was bad. Our teacher values constructive criticism over the typical “I liked it” or “I hated it”."
    
    a "It sounds like a good system."
    
    show carol smile
    
    c "It is!"
    
    show carol happy
    
    c "However, when opinions are too divisive, it can turn our workshop into an all-out war."
    
    show carol concerned
    
    c "...Some of us are especially sensitive when our writing is criticized."
    
    show carol neutral
    
    c "Me and the angry guy from before, we always fight on opposite sides, so now there’s some sort of rivalry between us."
    
    c "As I said, I don’t hate him, and he doesn’t hate me either. At least, I hope so... but sometimes things can get out of control."
    
    show carol angry
    
    c "...especially when you just know you’re in the right!"
    
    a "Did he… I don’t know, say something bad about a poem of yours?"
    
    show  carol concerned
    
    c "It’s a bit more difficult than that."
    
    show carol happy
    
    c "You see, today our teacher walked in with some pretty exciting news: we were all going to contribute to an anthology to showcase one of our better works."
    
    a "Oh, that’s good news, right?"
    
    a "Even if it’s only in an anthology, you’re still getting published! Congratulations."
    
    show carol smile
    
    c "Thanks! It is definitely good news."
    
    show carol concerned
    
    c "Good news, but…"
    
    a "But?"
    
    c "He told us to decide the order of our poems by ourselves."
    
    a "..."
    
    c "..."
    
    "I don’t really see why that would be a bad thing, but she clearly thinks the other way around."
    
    a "I-I see. That’s not great… right?"
    
    show carol smile
    
    c "Yup, not great at all!"
    
    a "..."
    
    show carol happy
    
    c "You have no idea why, right?"
    
    a "Please enlighten me."
    
    "Carol cleared her throat, preparing herself to explain."
    
    c "So, remember how I said artists are very prideful people? So of course some of us want to take the first few pages for ourselves."
    
    c "You see, in an anthology, the first work is also usually one of the better ones: it needs to grab the reader, make them see that there’s something of value inside the book, and hopefully convince them to stick around for a while longer."
    
    show carol angry
    
    c "Being first is proof that your writing is good enough to produce that effect in others."
    
    c "With each passing poem, the possibility of people losing their interest and forgetting about the book grows bigger."
    
    show carol happy
    
    c "Of course, you won’t put anything in the anthology that’ll bore them to death on purpose! But sometimes it does happen."
    
    c "So… you see where I’m getting at."
    
    "I had a general idea."
    
    a "Basically, it’s like a ranking. And those who rank lower…"
    
    show carol concerned
    
    c "Yeah. It’s not great if you’re at the back of the book. That’s why, if possible, you wish to be placed close to the beginning: it gives you a higher chance of being read."
    
    c "We met after class today to decide on the order… and it didn’t turn out well."
    
    c "Everyone thinks too highly of their own writing; no one wants to stand at the bottom of the pole, myself included."
    
    show carol angry
    
    c "Now you see why it’s so much trouble."
    
    "Human pride was something I could understand much better than poetry, so I did get the gist of the situation."
    
    "However..."
    
    a "Your teacher should’ve known this was going to happen. HE should’ve been the one to choose, not you guys. Can’t you say something about it?"
    
    show carol happy
    
    c "He’s not the type of guy who’d listen. And we need to learn to concede whenever someone is clearly better than you in your field."
    
    a "But that other guy isn’t."
    
    show carol angry
    
    c "No, he isn’t, but he still wants to be featured before me. That’s what we were arguing about."
    
    hide carol angry with dissolve
    
    "Carol’s worries sounded small, like a trivial argument among co-workers, nothing that she couldn’t overcome through sheer force of will."
    
    "Yet Carol, whose radiance at times blinded me, looked restless, more than I’d ever seen."
    
    "It sounded like a small deal, but to her it was anything but."
    
    "Publishing a book, even if it was only as a contributor, was her first step into the literary world."
    
    "Nothing short of a huge deal for a girl who’s dreamt all her life to be a writer."
    
    "In this situation, how could I support her? By offering a solution? By listening in complete silence?"
    
    "I cared for her, but I didn’t know which was the best way to act."
    
    "I wanted to make her worries go away… but I didn’t know how to proceed."
    
    "My inability to make a move frustrated me further."
    
    show carol concerned with dissolve
    
    c "Really, I don’t know what to do..."
    
    "I should’ve said something, anything."
    
    jump return3
    
    label return3:
    
    menu:
        "Encourage her.":
            jump return3
            
        "Stay quiet.":
            jump choice3
            
    label choice3:
    
    "But yet again, with my sight set on the ground, I remained silent, without changing a single thing."
    
    c "Maybe I could try to reach a compromise."
    
    "Carol didn’t seem pleased at the thought."
    
    c "As long as I’m published, I really don’t mind making a few sacrifices along the way."
    
    "But she minded, and a lot. It was crystal clear by the way she talked."
    
    show carol neutral
    
    c "Yeah, if worse comes to worse, that’s what I’m going to do. Do you think it’s a good idea?"
    
    a "If you’re ok with it, then make a compromise."
    
    pause 1.5
    show carol happy
    
    c "...then I will."
    
    show carol smile
    
    c "Yup, a compromise! That’s going to work out alright!"
    
    "She raised her fists, a radiant smile on her face."
    
    a "Now that’s the Carol we’ve all come to know and love."
    
    show carol happy
    
    c "Falling for me again?"
    
    a "Not in a million years."
    
    hide carol happy with dissolve
    
    "The sun was still up in the sky, but neither of us felt like walking any longer."
    
    "We stopped by the entrance of an old restaurant and lazily stared at people walking in and out."
    
    "I looked at my surroundings and didn’t quite recognize where I was. Though I knew we could retrace our steps to return, to be lost was still a scary feeling."
    
    "Carol seemed preoccupied by her own thoughts; weighing her options, I guessed."
    
    "She took a quick glance at me, but soon returned it to the streets."
    
    a "Come to think of it, why did that guy look at me the way he did?"
    
    show carol happy with dissolve
    
    c "What do you mean?"
    
    a "He just stared at me… it was weird. I remember he asked if I was a writer."
    
    show carol angry
    
    c "Oh, yeah. Young writers usually attend public readings and stuff, so they all get to know each other eventually. You knew me, so he assumed you had to be a writer."
    
    a "That’s a bit weird, isn’t it?"
    
    a "Of course you’d have friends that are not writers."
    
    show carol happy
    
    c "Who knows. I don’t have many friends, you know?"
    
    "Carol was a cheerful and friendly person who could make you open up to her in the brink of an instant."
    
    "It was difficult for me to imagine her as someone with few friends."
    
    show carol angry
    
    c "But yeah, it WAS rude!"
    
    show carol smile
    
    c "Don’t worry though: I’ll show him!"
    
    show carol happy
    
    c "After the anthology, I’ll compile some of my poems, get some help from my teacher and then I’ll try to publish them myself."
    
    a "Good luck. I hope you make it."
    
    c "But regardless of how it all ends, I’ll…"
    
    show carol concerned
    
    c "..."
    
    show carol happy
    
    c "No, forget about it."
    
    scene bg blackscreen with dissolve
    pause 2
    
    "We headed back home soon after. Carol, looking better than before, said she had to make some calls and work on her poems before their next meeting."
    
    "I returned to my dreamless routine, hoping the best for my friend."
    
    stop music fadeout 1
    
    pause 2
    
    scene bg bedroom2 with dissolve
    pause 2
    
    play music "scene 2.mp3"
    
    "And then, in the blink of an eye, winter came."
    
    "One rarely notices the subtle changes in temperature that mark the end of autumn; by the time we decide to look up, the colorful leaves adorning the trees have already fallen."
    
    "I wouldn’t say I enjoyed winter; I wouldn’t say I hated it either."
    
    "The cold comes with its ups and downs: waking up is hard, and the road to school feels more like an odyssey than ever."
    
    "Yet people begin to avoid the outside world to their utmost, and so, once-busy streets suddenly become empty."
    
    "Walking across a seemingly-deserted town feels nice. It’s like entering an old world where humanity has ceased to exist, leaving only traces of their civilization behind."
    
    "Of course, the illusion breaks soon enough whenever another person decides to pass by."
    
    "For a while, however, I’m free to imagine myself alone in the world, which is a surprisingly pleasant feeling."

    play sound "unlock door.wav"
    pause 1
    scene bg blackscreen with dissolve
    play sound "door close.wav"
    pause 1
    
    "By this time of the year, students begin to wish for their share of solitude, as if consumed by the freezing atmosphere in the air."
    
    "Winter equals exams, after all. Loads of them. Enough to fill your head with worries over whether or not your grades are good enough to save the semester, stress oozing from every inch of your body."
    
    "Needless to say, I was going through such a predicament."
    
    "And so was Carol."
    
    scene bg building outside with dissolve
    
    "The both of us had locked ourselves in our apartments, willing to spend days, if not weeks, reviewing our respective material and finishing assignments due the following mornings."
    
    "Irregular schedules and a duty to keep studying, no matter the circumstances, had decreased the number of times we met every week."
    
    "We texted each other, exchanging small jokes to make the studying a little more bearable, but we didn’t see each other nearly as much."
    
    "I didn’t hear her voice for over 2 weeks."
    
    "It might sound strange, considering we were neighbors, but there was really nothing weird about it."
    
    "Carol was the type of person who wouldn’t stop studying until her exams were over."
    
    "Me, well… I was never an exemplary student: I did what I had to do and nothing more than that."
    
    "But seeing Carol put so much effort into it made me want to try a little bit harder myself."
    
    "Besides, I didn’t want to distract her in such a crucial time."
    
    "After our conversation from a few months back, she had never again mentioned anything related to the compilation."
    
    c "“I’m working on a few poems right now.”"
    
    c "“I believe this is turning out good.”"
    
    "I’d hear small comments such as these, but never anything concrete."
    
    "Sometimes I found myself thinking about it."
    
    "”Maybe I should call and ask.”"
    
    "”...but if she doesn’t want to tell me, then I can’t force her.”"
    
    "”What if she does want to tell me?”"
    
    "”No. If she did, she would’ve told me herself.”"
    
    "I’d often have this conversation with myself, and I’d always reach the same resolution."
    
    "I thought I wouldn’t hear from Carol again until after she was done with her exams."
    
    "That is, until I got a call from her."
    
    play sound "cell vibrate.wav"
    pause 2
    queue sound "cell vibrate.wav"
    pause 2
    
    c "‘Sup dude! How’s it going?"
    
    a "Alright, I guess. I just stepped out for a bit to get some fresh air."
    
    c "Yeah, I see you from up here. Isn’t it freezing?"
    
    a "Not so much."
    
    c "Do you have some time to hang out? If so, I’m coming down."
    
    a "Sure. I’ll wait for you by the door."
    
    pause 2
    
    "Moments later, Carol stepped out of the building, sweating in some unnatural way."
    
    show carol smile with dissolve
    
    a "Did you just run down the stairs?"
    
    show carol angry
    
    c "The elevator was taking way too long!"
    
    a "You’re going to get a chill that way, with this weather."
    
    show carol happy
    
    c "You should know by know that I’m sturdier than I look."
    
    c "How’s it going, Alan?"
    
    a "Same as always."
    
    a "How’s school, Carol?"
    
    show carol smile
    
    c "I should be ok for most of my classes. You?"
    
    a "Trying my best not to fail everything."
    
    show carol happy
    
    "She patted me on the back."
    
    c "Don’t worry dude! You’ll make it if you try."
    
    a "Let’s hope that’s the case."
    
    a "I’ve been trying… and for real, this time. Not like last year."
    
    "Carol nodded in agreement."
    
    show carol smile
    
    c "Yup, I know. You’ve grown so much!"
    
    "She proceeded to mess with my hair."
    
    show carol happy
    
    "It was a bit awkward because of our height difference, but somehow she stretched enough to reach my head with the tips of her fingers."
    
    "She was trying to make fun of me, but her touch felt so tender that I just let her do what she wanted."
    
    "Carol stayed like that, on her tiptoes, for a while that felt like an eternity."
    
    show carol blush with dissolve
    pause 2
    show carol neutral with dissolve
    
    "It doesn’t take me long to feel that something’s wrong."
    
    a "Carol? Are you ok?"
    
    show carol happy
    
    c "I’m doing just fine."
    
    "And in saying so, she stepped away from me, looking just like always."
    
    "Was it my imagination?"
    
    show carol smile
    
    c "Maaaan, it’s been ages since I last went outside! It’s nice feeling the air on my cheeks again, even if it’s cold as fuck."
    
    a "Have you been locked in your apartment all this time? That’s not very good for you."
    
    show carol happy
    
    c "It’s alright. Julian has been buying the groceries in my stead, and it’s all well as long as I keep cooking."
    
    c "Being a shut-in is honestly not as bad as it seems."
    
    a "Come to think of it, is Julian doing alright?"
    
    c "He’s the same as always. Still trying his hardest, still putting up with my selfishness."
    
    c "Truly the ideal boyfriend."
    
    "Yet there was a fair air of uncertainty mixed in her words, as if she wanted to add something else, but couldn’t."
    
    a "Did… anything happen?"
    
    show carol concerned
    
    c "..."
    
    show carol happy
    
    c "...not really. Just a bit of fighting going on the side. Same as usual."
    
    c "Nothing you should worry about."
    
    "Carol put her hands together and timidly played with her fingers."
    
    "It seemed she had something to say, but didn’t know how to put it into words."
    
    "It was somewhat worrying."
    
    a "Did he hit your or something?"
    
    show carol angry
    
    c "N-no! What would make you think that? You know that Julian would never dare put a finger on me!"
    
    a "O-ok, I’m sorry."
    
    "Her anger seemed genuine, so she must’ve been telling the truth."
    
    show carol happy
    
    "There was something wrong with her, but asking didn’t feel right, and I didn’t believe Carol would feel comfortable sharing it with anyone."
    
    "Even if it was me."
    
    jump return4
    
    label return4:
    
    menu:
        "Ask what's wrong.":
            jump return4
        
        "Drop the subject.":
            jump choice4
                
    label choice4:
        
    a "I’ll drop the subject then. I’m sure you don’t want to talk about it."
    
    show carol neutral
    
    c "..."
    
    "I was about to suggest going back inside or walking to the nearby café."
    
    stop music fadeout 1
    
    c "I kinda hate it when you say that, Alan."
    
    "But my proposal had no time to escape my throat."
    
    play music "scene 4.mp3"
    
    a "...you hate it when I say what?"
    
    c "“I won’t ask“, “I’ll drop the subject“, “let’s talk about something else.“"
    
    show carol happy
    
    c "It really pisses me off sometimes."
    
    "She said with a smile, so I couldn’t quite take her words seriously."
    
    c "Do you understand why, Alan?"
    
    "I came up with a few options, but none of them felt like the answer she was searching for."
     
    "I gave up, and it showed."
    
    show carol neutral
    
    "Carol sighed deeply."
    
    c "If you don’t, then I’m not going to tell you."
    
    c "But y’know, trying to be so considerate all the time can backfire if you’re not careful. Have you ever thought of that?"
    
    a "I… don’t think of myself as an especially considerate person."
    
    show carol happy
    
    c "But you are. You’re a considerate, kind and sweet person, even if it doesn’t show because you don’t talk too much with others."
    
    show carol neutral
    
    c "At least, you always try your best to never make me sad."
    
    show carol smile
    
    c "And that’s great! It shows that you’re a good person deep inside. It’s something I’ve really come to appreciate about you this past year!"
    
    show carol happy
    
    c "But, y’know… too much of a good thing can turn into a bad thing, or so the saying goes."
    
    show carol neutral
    
    c "...do you get what I’m trying to say?"
    
    a "..."
    
    c "I see."
    
    hide carol neutral with dissolve
    
    "We both fell silent."
    
    "While I did want to say something, there was nothing else to add."
    
    "While I did want to change the subject, maybe go for a quick stroll, it wasn’t possible with her in front of my eyes."
    
    "While I did want to run away, escape, seek shelter below the sheets of my bed, my body was dead cold, and it wouldn’t move."
    
    show carol neutral with dissolve
    
    "We looked into each other’s eyes."
    
    show carol concerned
    
    "Surprisingly, Carol was the first one to give up."
    
    c "I’m sorry. I didn’t mean to say all of that. We were supposed to be down here to catch a break, but I…"
    
    a "No, it’s ok. I’m pretty much at fault on this one... or maybe no one is really at fault."
    
    a "Yeah, let’s go with that."
    
    show carol happy
    
    c "Sure!"
    
    a "Still, I’ll keep your words in mind."
    
    show carol neutral
    
    a "It was somewhat flattering to hear you say that I’m a kind person."
    
    a "No one has ever said that to me before."
    
    show carol smile
    
    c "It was quite embarrassing to say! I’m not going to repeat it, ok?"
    
    show carol happy
    
    c "And don’t forget about the important part."
    
    a "I won't ma'am."
    
    show carol smile
    
    c "Excellent."
    
    hide carol smile with dissolve
    
    stop music fadeout 1
    
    scene bg blackscreen with dissolve
    
    "We decided to go back inside shortly afterwards."
    
    "We took the elevator; the closed space warmed us up."
    
    "Walking side by side with her felt awkward after our talk… but it wouldn’t change much between us: friends have these sorts of arguments every now and then."
    
    "If you could even call that an argument."
    
    "Carol pulled out her keys to unlock the door to her apartment."
    
    show carol happy with dissolve
    
    c "Oh yeah, there’s something I should tell you."
    
    play sound "unlock door.wav"
    pause 1.5
    
    c "After I’m done with my exams in a few weeks… I’m going back home."
    
    c "Like, forever."
    
    a "..."
    
    a "Oh."
    
    c "I'll tell you about it later, ok?"
    
    a "..."
    
    a "Ok."
    
    show carol smile
    
    c "See ya!"
    
    hide carol smile with dissolve
    play sound "door close.wav"
    pause 2.5
    
    a "See ya."
    
    "The door closed in front of my eyes, and I could only respond by planting my feet on the ground, unsure of what to do or think."
    
    pause 2
    
    scene bg bus station with dissolve
    play music "scene 1.mp3"
    pause 2
    
    "The moment came sooner than I had expected."
    
    "Hail fell down on our heads for the first time in many years, and with it, school semesters all around the country came to an end."
    
    "Without even waiting to see the fruit of her efforts, Carol packed up and bought a bus ticket back home."
    
    "Her reasons were many, but they could all be boiled down to one:"
    
    show carol happy with dissolve
    
    c "Basically, nothing worked the way I hoped."
    
    hide carol happy with dissolve
    
    "The anthology was the first wall to fall apart."
    
    "Though she tried to reach a compromise, it turned out to be impossible for her, and in the end the group never reached an agreement."
    
    "Their teacher, apparently disappointed at their inability to see the flaws in their own craft, decided to postpone the project until further notice."
    
    "That notice never came."
    
    "At odds with her companions, and feeling that she wouldn’t get anything else out of that workshop anymore, Carol left the group soon afterwards."
    
    "Out of confidence of her own writing, she still held up some hope."
    
    "Desperately, she knocked on the door of every small-time publisher in town, begging them to take a look at her work."
    
    "Half of them ignored her pleas."
    
    "The other half looked at her poems, applauded some of them, but eventually concluded the overall quality wasn’t good enough for a book."
    
    "“But you have talent, so keep trying”, they said."
    
    scene bg bedroom with dissolve
    pause 1
    
    "Out of a dozen of meetings, Carol got only a couple of emails, and not much else."
    
    show carol concerned with dissolve
    
    c "I’m not good enough to survive in that world on my own…"
    
    c "At least, not yet. That’s what I got out of the experience."
    
    hide carol concerned with dissolve
    
    "That wouldn’t have been enough to break her spirits, however."
    
    "She wasn’t good enough… “yet”."
    
    "But if she kept working on her craft, while balancing her studies on the side, sooner or later she’d reach the level editors desired of her."
    
    scene bg street1 with dissolve
    
    "But one night, as she was preparing herself to call her old teacher for a chance to go back to the workshop, Julian, her boyfriend, approached her."
    
    show carol neutral with dissolve
    
    c "He told me he was going back home."
    
    c "I asked him why."
    
    c "He said that his father was sick, and that he wouldn’t be able to take care of her mother anymore."
    
    show carol concerned
    
    c "He’d been thinking about it for a long time, apparently."
    
    c "Julian practiced, and practiced, but never felt the same passion for music as he once did."
    
    c "Studying at that school, competing for rewards he didn’t desire…"
    
    show carol neutral
    
    c "He was making himself unhappier with each passing day."
    
    c "And I noticed as well, how lately he hadn’t been acting as himself."
    
    show carol happy
    
    c "And well… even though he told me I could stay, I decided to go with him."
    
    hide carol happy with dissolve
    
    "Despite everything, she loved Julian, and she feared that by living apart, everything they had worked so hard to build together might’ve crumbled away."
    
    scene bg street2 with dissolve
    
    "Deep inside, Carol feared she wouldn’t be able to make it without Julian’s support."
    
    show carol smile with dissolve
    
    c "But I’m not giving up, y’know?"
    
    show carol happy
    
    c "I’ll keep working, and little by little I’ll get better. I did get some e-mail addresses, so if I write anything good I’ll send it their way."
    
    c "I’ll do it. No matter how much time it takes, I’ll do it."
    
    show carol smile
    
    c "Just you see!"
    
    hide carol smile with dissolve
    
    "I could only mutter a half-hearted “I believe in you”."
    
    "Needless to say, I never knew about any of this: Carol told me only a few days prior."
    
    scene bg bus station with dissolve
    
    "We walked together to the station."
    
    "Julian wasn’t with us, as he had returned a few days ago to prepare everything beforehand."
    
    "There wasn’t much to talk about on the way there: everything had more-or-less been said before."
    
    "It was early in the morning, but there were still a lot of people around, possibly so they could get to their destinations while the sun was still out."
    
    "Carol’s hometown was 12 hours away from there."
    
    "I realized I’d never even thought of making such a long trip in my life."
    
    "It dawned on me just how far away she was going; how our afternoons just chatting on Carol’s terrace were not going to be possible anymore."
    
    "We lived in an extremely convenient era where I could just pick up the phone and talk with her anytime, and it was even possible to see each other through our computer screens."
    
    "I tried to reassure myself thinking that living half a country away wouldn’t be a problem, not with the current technology."
    
    "However, deep down, I knew it wouldn’t be the same."
    
    show carol happy with dissolve
    pause 2
    
    "Carol smiled, just like she always did."
    
    "She never ceased to smile, even as she told me about all the problems she’d had."
    
    "I had too many questions I wanted to ask."
    
    "Why did she never tell me anything about this?"
    
    "Wasn’t there a way to convince Julian to stay? Couldn’t she stay, even if Julian wasn’t by her side?"
    
    "Why wouldn’t she trust me with her problems, with her secrets, with her company?"
    
    "But as always, I remained silent."
    
    "The air in the station was cold, but leaning on each other’s shoulders as we waited for Carol’s bus to arrive made the experience a little more bearable."
    
    a "Do you have everything you need?"
    
    c "Mhm."
    
    a "Did you sort everything out with the landlord?"
    
    c "Yup, everything's ok."
    
    a "You sure you're not forgetting anything, right?"
    
    show carol angry
    
    c "Jesus Alan, stop acting like my mom!"
    
    c "Everything's fine, seriously."
    
    a "Sorry, sorry. I'm just..."

    show carol happy

    "I couldn’t explain my exasperation, but Carol seemed to understand regardless."
    
    "Buses came and went, people stepped in and out, and we waited, sharing our body heat as our only means of communication."
    
    "And the one she was waiting for arrived."
    
    show carol smile
    
    c "There it is!"
    
    hide carol smile with dissolve
    
    "The speakers signaled that the bus was going to depart in a few minutes."
    
    "Defeated, I followed Carol to the platform."
    
    "People were loading their luggage and showing their tickets."
    
    "Carol did the same, handing over the few bags she was carrying."
    
    show carol happy with dissolve
    
    c "I guess this is it then."
    
    "My heart sunk, and I was unable to look her in the eye."
    
    show carol concerned
    
    c "Hey, c’mon. Don’t look so sad Alan; you’re going to make it hard for me as well."
    
    a "Yeah, I know. You're that type of person."
    
    show carol smile
    
    c "Yup, so cheer up! C’mon, show me a smile!"
    
    "I tried my best to do what she wanted."
    
    show carol happy
    
    c "...that’s a very unconvincing smile, but it’ll have to do."
    
    "Carol knew she needed to step in and find her seat, but she stayed outside, looking at me somewhat nervously."
    
    "Just like me, she wasn’t sure how to bid her farewells."
    
    show carol blush
    
    c "Come over here for a bit."
    
    hide carol blush with dissolve
    
    "I did as she said, and I felt her arms slowly wrapping around my chest."
    
    "Though taken aback for a second, I made haste to embrace her back."
    
    a "I’m going to miss you."
    
    c "I know."
    
    c "I'll miss you too."
    
    "Her warmth stayed with me, even as we separated."
    
    "My mind felt numb; my heart felt hot."
    
    show carol happy with dissolve
    
    c "Goodbye, Alan."
    
    a "See you around."
    
    hide carol happy with dissolve
    
    "As I said those words, Carol turned around and prepared to climb the steps into the bus."
    
    a "Carol!"
    
    show carol neutral with dissolve
    
    "She stopped under the threshold, and turned around to face me."
    
    a "..."
    
    menu:
        "“Take care of yourself.“":
            jump choice5a
        "“I love you.“":
            jump choice5b
    
    label choice5a:
        
    a "Take care of yourself."
        
    "Somehow, I managed to stop myself from saying something I shouldn’t."
    
    show carol smile

    c "...yeah, you take care as well."
        
    hide carol smile with dissolve
        
    "Carol showed me a warm smile from the other side of the glass as the doors closed, and the bus took off."
        
    "Motionless, I stared at the machine as it drew Carol further away from my sight, until I could no longer see her silhouette standing by one of the windows."
        
    "Just like any of the countless unimportant farewells that took place on that station, ours’ ended, unnoticed by everyone but ourselves."
        
    "Was that the right choice to make? I don’t know, and I’ll probably never know."
        
    "It could’ve changed something in our lives, just like it could’ve been completely meaningless."
        
    "I don’t regret nor curse myself for keeping my mouth shut that day."
        
    "Only, when I think back on the whirlwind of emotions convoluted in my chest at the time, my heart sinks a little."
        
    "Not for what it could’ve been, but for what it was."
        
    "Even back then I knew that those would be the last words I’d exchange face-to-face with Carol."
        
    "The thought alone, no matter how hard I tried to sugarcoat it, was depressing enough to cry."
        
    jump choice5c
        
    label choice5b:
        
    "The thought of spouting those words and possibly changing something between us was scarier than anything I could ever imagine."
    
    "However, she explained herself well enough: how she hated whenever I avoided saying the things I wanted to say."
    
    a "I love you."
        
    "The words had a hard time crawling out of my throat, but somehow I managed to express my feelings."
        
    show carol blush with dissolve
    pause 2
        
    c "Yeah."
        
    hide carol blush with dissolve
        
    "She hopped out of the bus, to the annoyance of the driver, who just wanted to leave the station at once."
        
    "It was for a brief moment, but I felt her cold lips rubbing against my cheek."
        
    "Her hands rested on my shoulders, and she sighed, placing her head on my chest."
        
    show carol blush with dissolve
        
    "Finally, Carol stepped back."
        
    "She blushed, though I couldn’t tell if it was because of the cold or the kiss."
        
    c "I love you too."
        
    hide carol blush with dissolve
        
    "The driver was hurrying her up. She quickly stepped into the bus, but our eyes stood their ground, gazing directly at each other."
        
    show carol smile with dissolve
        
    c "Don’t forget to call!"
        
    hide carol smile with dissolve
        
    "The door closed."
        
    a "I won't!"
        
    "Her voice was muffled by the door between us and the roaring engine, but I could still make out her answer."
        
    c "You better, or else I won’t forgive you!"
        
    c "And thanks for everything!"
        
    "Motionless, I stared at the machine as it drew Carol further away from my sight, until I could no longer see her silhouette standing by the window."
        
    "In the end, my choice didn’t change a thing about our relationship."
        
    "Carol didn’t reject me, nor did she stay by my side."
        
    "I laughed at how nervous I had felt before professing my love."
        
    "I understood almost immediately: her “love” wasn’t the same as mine. She cherished me, but not in the way I had hoped."
        
    "Otherwise she wouldn’t have left."
        
    "Still, it made me somewhat happy to know that I was important to her, to some degree."
        
    "I don’t regret nor curse myself for saying those words that day."
        
    "Only, when I think back on the lethargic happiness that took over my mind after her departure, my heart breaks a little."
        
    "Not for what it could’ve been, but for what it was."
        
    "Even back then I knew that those would be the last words I’d exchange face-to-face with Carol."
        
    "But the thought wouldn’t cross my mind for a while."
        
    jump choice5c
        
    label choice5c:
        
    stop music fadeout 1
    scene bg blackscreen with dissolve
    pause 2
    scene bg bedroom2 with dissolve
    play music "scene 2.mp3"
    
    "We stayed in contact with each other via texting and occasional phone calls."
    
    "Our conversations were never meaningful: we’d mostly talk about recent developments in our lives for 5 or so minutes before hanging up."
    
    "Things began to go a bit better for Carol once she returned to her parents’ house."
    
    "She took a short teaching course over there, enough to get some small tutoring jobs for a steady monthly income."
    
    "As I expected, she never gave up on writing."
    
    "She kept composing poems, drawing inspiration from the humid forests around her hometown."
    
    "Her efforts bore fruit, and a publisher finally took enough of an interest in her to publish a small compilation of her works."
    
    "She sounded genuinely overjoyed when she told me about it."
    
    "Carol never talked about Julian, but I could sometimes hear his voice over the phone, and assumed they were still together."
    
    "Her family seemed to be supporting her as well, to the best of their abilities."
    
    "I was glad."
    
    "On my front, things kept moving in the same direction as always."
    
    "I continued with my studies, I continued with my relationships, I continued with my life."
    
    "Carol’s departure was but a small mishap that changed close to nothing in my everyday routine."
    
    "Someone else moved into her apartment; I never got to talk to them for more than a few seconds."
    
    "There’s nothing of particular importance to add."
    
    "None of that feels important, in retrospect."
    
    "What’s important from where I currently stand is only what’s related to Carol."
    
    "How communication between us gradually began to fade away."
    
    "...I say that, but there’s not a lot to explain."
    
    "Just like with every long distance relationship between two individuals who lead far too different lives, we ceased to talk with each other simply because we had more important things to care about."
    
    "For her, writing good poetry was a far bigger priority than catching up with me."
    
    "For me, getting my degree and finding a good job was far more essential than knowing what she was up to."
    
    "I wouldn’t say that our friendship dwindled."
    
    "I, for one, still cherished her a lot."
    
    "There’s nothing dramatic about growing distant to one another."
    
    "Life is not a theater where every breach of relations can be explained through some teary-eyed backstory."
    
    "We were simply too busy to pick up the phone."
    
    "It just happened."
    
    "There was no one to blame."
    
    "That being said, I can’t ignore that some degree of regret rests in my heart."
    
    "Maybe I could’ve made the time to write a text message, and who knows, maybe Carol would’ve even replied."
    
    "Maybe part of me was scared of pursuing my friendship with her."
    
    "But right now, I don’t have the means to understand the thought process of my past self."
    
    "And so, with a plethora of things to keep me occupied, months passed, then a year, then two."
    
    "I was already out of college and worrying about my new office job."
    
    "Sitting behind a desk and ceaselessly typing on a computer is what I always imagined myself doing in the future."
    
    "I was never someone to dream big, to wish for a life of unfathomable success."
    
    "In that sense, Carol was something like my opposite, and probably why we got along so well."
    
    "People search in others what they’re lacking, or so I heard."
    
    "In my own search for partners that owned what I didn’t, I dated a couple of girls during that 2 years span, but none of my relationships lasted for more than a few months."
    
    "Deep down I just wasn’t sure where to go with my life."
    
    "I was content, but not necessarily happy."
    
    "I wanted something, but I didn’t know what."
    
    "Everyday was the same, but somehow more sluggish than the last."
    
    "It was a strange state of affairs: there wasn’t anything particularly bad about my life, and things were generally going pretty well. There was nothing to dislike."
    
    "Yet I wasn’t happy, and once I realized it, I began to feel frustrated as well."
    
    stop music fadeout 1
    pause 1
    c "For no reason at all, I woke up feeling like it was the worst day imaginable…"
    pause 1
    
    "I remembered the words Carol had spoken long ago, and wondered if it wasn’t only that morning, but every morning that she had felt like it was the worst day in her life."
    
    "Maybe, just maybe, I was finally being able to share part of the emotions that drove her to such lengths."
    
    "Our conversations, our lazy afternoons together, it all floated back to me as I gave the matter some thought."
    
    "I decided to call her, for the first time in a long while, just to know how she was doing."
    
    pause 2
    
    "For a moment, I feared that she might have changed her phone, but to my relief the call eventually connected."
    
    "I waited for a second."
    
    play sound "calling tone.mp3"
    pause 3
    
    "Two."
    
    play sound "calling tone.mp3"
    pause 3
    
    "Three."
    
    play sound "calling tone.mp3"
    pause 3
    
    "No one picked up."
    
    "I was redirected to leave a voicemail, but I decided against it. Maybe she had gone for a walk without her phone." 
    
    "Regardless, I was sure she’d call me back once she saw my missed call."
    
    scene bg blackscreen with dissolve
    pause 3
    scene bg bedroom2 with dissolve
     
    "And the next day came."
    
    play sound "cell vibrate.wav"
    pause 2
    queue sound "cell vibrate.wav"
    pause 2
    
    "My phone rang early in the morning."
    
    "Thinking that it had been my alarm, I ignored it and waited until it stopped."
    
    play sound "cell vibrate.wav"
    pause 2
    queue sound "cell vibrate.wav"
    pause 2
    
    "A few minutes later, I got called again."
    
    "This time, however, I was fully awake."
    
    "Looking at the screen, it was a number I couldn’t recognize."
    
    pause 2
    
    a "Yes?"
    
    a "..."
    
    a "Is someone there?"
    
    j "Is this Alan?"
    
    "I remained silent, trying to recognize the voice."
    
    a "Julian?"
    
    j "Yes. It’s been a while, Alan. One, two years?"
    
    "Out of everyone, I wasn’t expecting to receive a call from Carol’s boyfriend himself."
    
    a "What’s up dude? How’s Carol doing?"
    
    a "I called her yesterday, but she didn’t pick up."
    
    j "I know."
    
    j "..."
    
    a "Julian? Something wrong?"
    
    j "Alan, are you sitting down right now?"
    
    "That was a strange question."
    
    a "Yes, I am."
    
    j "Then I’ll try not to dodge around the subject, and I’ll say it straight away."
    
    pause 2
    
    "There was a brief silence on the other side of the line."
    
    "I used that frame of time to quickly stretch my hand and grab a glass of water I had by the bedside."
    
    j "Carol is dead, Alan."
    
    a "..."
    
    j "She died a few days ago. I just saw your call on her phone, so I thought I’d let you know."
    
    j "...I'm sorry."
    
    pause 4
    
    "It’s difficult to explain my first reaction upon hearing those words."
    
    "Somehow it wasn’t sadness, or surprise."
    
    "It felt closer to a mild sense of confusion or disorientation, as if, for a moment, I couldn’t recognize my room, or remember who I really was."
    
    "Everything looked unreal out of sudden, like part of some twisted but mundane fantasy; a boring and cruel fantasy."
    
    "The words didn’t feel real, and thus, everything ceased to be real, and I became lost in a foreign realm."
    
    "But for a moment."
    
    "Only for the briefest, most miserable of moments."
    
    a "How did she die?"
    
    j "Carol, she..."
    
    a "How did she do it?"
    
    "My voice must’ve sounded horrifyingly calm to Julian, who choked on his words when trying to respond."
    
    a "Just don’t lie to me… please."
    
    j "...yes, she killed herself."
    
    a "When’s the funeral?"
    
    j "The wake and the funeral are the day after tomorrow."
    
    a "I'll be there."
    
    a "Can you tell me the address, or anything I should need to know?"
    
    "Me and Julian briefly talked about how to get to Carol’s parents’ house, which is where everything was going to take place."
    
    a "I'll see you there."
    
    j "Yes. I'll see you."
    
    "We hung up at the same time."
    
    play sound "breaking glass.wav"
    pause 3
    
    "I threw the glass of water in my hand to the wall, with all the strength I could muster."
    
    "The glass shattered on impact."
    
    "Dozens of pieces flew off all around the room, turning the ground into a field of deadly mirrors."
    
    a "Fuck."
    
    "Life began to look obscenely hateful through my many reflections on the glass shards."
    
    a "Fuck!"
    
    scene bg blackscreen with dissolve
    pause 3
    
    centered "And then I screamed."
    centered "I punched."
    centered "I ripped."
    centered "I gutted."
    centered "I dissected."
    centered "I dismembered."
    centered "I beheaded."
    centered "I murdered."
    centered "I bastardized."
    centered "I crushed."
    centered "I cut."
    centered "I smashed."
    centered "I tortured."
    centered "I profaned."
    centered "I destroyed."
    centered "I annihilated…"
    
    pause 2
    
    centered "...I anguished."
    centered "I cried."
    centered "I despaired."
    centered "I suffered."
    centered "I drowned."
    centered "I burned."
    centered "I crashed."
    centered "I grieved."
    centered "I agonized."
    centered "I distressed."
    centered "I repulsed."
    centered "I repelled."
    centered "I hated."
    centered "I cursed."
    centered "I resented."
    centered "I loathed."
    centered "I scorned…"
    
    pause 2
    
    "I got tired."
    "The room was a mess."
    "I gave up."
    
    pause 2
    
    "I went to sleep."
    
    pause 3
    
    scene bg carol house with dissolve
    play music "scene 4.mp3"
    pause 2
 
    "I attended the wake."
 
    "It was a normal wake."
    
    "Considering I had never been to one of these before, it was a weird thing to say… but that’s the impression I got."
    
    "A normal wake."
    
    "Not a lot of people came, and barely any were of my age."
    
    "Carol wasn’t lying when she said she didn’t have many friends."
    
    "I greeted her parents, who could barely look at me in the face because of the tears that gathered in their eyes."
    
    "They looked like a respectable couple, the type who’d raise a respectable child."
    
    "...I’d say they did a good job."
    
    "I greeted Julian, who looked just like I remembered him."
    
    "It dawned on me that it had only been 2 years since I last saw him, and that people don’t change a lot in 2 years."
    
    "It was funny."
    
    "I laughed."
    
    "Understandably, he wasn’t amused by my reaction."
    
    "Through him I learned a lot about what Carol had gone through for the past couple of years."
    
    "It surprised me to hear that the two of them had broken up months before all of this."
    
    a "But you looked so good together."
    
    j "Sometimes things seem better than they are."
    
    a "I suppose you could say the same about this entire situation."
    
    j "Sadly."
    
    "I asked whether things had gone wrong in her life somewhere along the line."
    
    j "No. Things were gradually getting better, and she seemed to be making progress with her treatment."
    
    "Though she never brought it up again, I should’ve figured Carol never stopped visiting her psychiatrist."
    
    j "However, she looked dissatisfied… as if all the happiness she had was somehow not good enough anymore."
    
    j "And then one day…"
    
    "But I prompted him to stop. I didn’t want him to reflect on her death more than he already was."
    
    "Carol took her life a few days before I had made that call."
    
    "The method of her suicide had been the same as the one she’d attempted to use in the past."
    
    "Maybe, deep down, she believed it wouldn’t work."
    
    "Maybe, deep down, she thought it’d turn out the same way as before, and she’d come out of it with another funny story to tell."
    
    "There’s no way to know."
    
    "There’s also no need to undermine her intentions: she wouldn’t have swallowed those pills if her death wish hadn’t been real."
    
    "...but I didn’t want to dwell on that either."
    
    pause 2
    
    scene bg living room with dissolve
    
    pause 2

    "I sat before the coffin, alone in the living room of that empty house."
    
    "This is where the wake had taken place, and now only Carol was left to rest on her own until the time of her funeral."
    
    "The old couple wasn’t particularly religious, but they respected and were grateful of these rites."
    
    "Instead of mourning her at a chapel, however, they had decided to do it at home, where she lived."
    
    "They probably thought her spirit would feel more at ease here."
    
    "It took me a lot of courage to step in and bid my farewells to the body."
    
    "I remember thinking that Carol looked thinner than before, but otherwise I felt nothing upon seeing her face for the last time."
    
    "I had already accepted her death; specifically, during the bus ride to this place."
    
    "But after her family members were gone, and everyone had left to attend to their own issues, I suddenly wished to enter that room again."
    
    "It wasn’t to see her face again, it wasn’t to cry over her coffin…"
    
    "I simply wished to enter that room."
    
    "Her parents were a bit dubious to let me in, but Julian managed to convince them."
    
    "He needed only to say the following:"
    
    j "He was her best friend."
    
    "So I was, huh?"
    
    "I felt both honored and disgusted at myself."
    
    "Even after all this time, I never guessed how important I was to her, or how much she might have needed my support."
    
    "I failed her, and I’d have to live with that for the rest of my life."
    
    "It’s only torturous… and maybe a little bit sad."
    
    pause 3

    "And so I sit here."
    
    "In this empty room."
    
    "Where no other living being stands."
    
    "Retelling to my tired ears, over and over again, the story I shared with her."
    
    "I feel only memories, slipping away from my mind, enchanting with their voice the corpse of the woman I once loved."
    
    "I can see them trying to reassemble her body."
    
    "They take her eyes from one fragment of my past; her smile, from another."
    
    "They try their best, they attempt to recreate this ambivalent girl in front of my eyes."
    
    "A shade of her existence begins to form."
    
    "It’s not enough."
    
    "My memories try even harder."
    
    "They use the skin of the girl lying in that coffin as a template for their replication."
    
    "At last, she appears before my eyes."
    
    show carol blur with Dissolve (1)
    
    "What stands before me is only a phantom of her past self -her lifeless eyes are solid proof of that- but nevertheless it evokes the same warmth in my heart as she did."
    
    "It’s Carol."
    
    "She looks genuinely happy."
    
    "Is she happy because she finally managed to meet with death?"
    
    "Is she happy because she didn’t have to suffer silently anymore, as she always had?"
    
    "Is that it?"
    
    c "..."
    
    "...no, it doesn’t seem so."
    
    "Then is she happy because I’m here, to chat with her one last time?"
    
    c "..."
    
    "...that seems to be it."
    
    "Even if it’s only my imagination, I’m pleased to know that my presence means so much to her."

    a "Would you have been happier if I had visited while you were still alive?"
    
    "She doesn’t respond."
    
    "However, now that I’ve opened my mouth, I wish to keep talking, to keep indulging in this fantasy."
    
    "Carol never liked it when I didn’t say what I wanted to say."
    
    a "How have you been, Carol?"
    
    a "Sorry it took me so long to get here."
    
    a "Are you… angry with me?"
    
    c "..."
    
    a "I’m glad, though to be honest, I believe you should be."
    
    a "I made too many mistakes to be forgiven."
    
    c "..."
    
    a "Because you gave me a myriad of hints, but I ignored them all."
    
    a "You know what I’m talking about, right?"
    
    c "..."
    
    a "I never did anything for you… or rather, I never tried to do anything for you."
    
    a "Was I too afraid to hurt you? Is that why I always kept my questions to myself, why I avoided the difficult topics as much as I could?"
    
    a "Maybe. And maybe I would’ve hurt you… but in the end, it would’ve been for the best."
    
    a "It might have been difficult, but it would’ve gotten the point across."
    
    a "That I cared for you, and that I wanted to be there for you, as your best friend."
    
    a "My inability to act made you believe I didn’t trust you enough… the same way I thought you didn’t trust me enough."
    
    a "In the end, we just needed to stop mumbling around and just… talk."
    
    a "Talk about the important stuff, without the fear of angering or saddening each other."
    
    a "I would’ve loved to see you angry or sad."
    
    a "Your eternal smile was the most unnatural thing in the world."
    
    a "Only now I can say so."
    
    a "I’m sorry."
    
    "I take a quick breath."
    
    c "..."
    
    a "Yes, when you told me about your first attempt."
    
    hide carol blur with dissolve
    
    scene bg bedroom with dissolve
    show carol happy with dissolve
    pause 2
    
    a "I didn’t know what to do, I didn’t know what to say."
    
    a "You put me on the spot, y’know? I wasn’t supposed to have an answer ready for that."
    
    a "...yes, I know."
    
    a "When you were about to explain the reasons of your attempted suicide, as painful as they could’ve been."
    
    c "No, you don’t want to hear it."
    
    "I should’ve said..."
    
    jump finalchoice1
    
    label finalchoice1:
        
    menu:
        "“Please tell me.“":
            jump finalchoice1a
        
        "“You probably don't want to talk about it.“":
            jump finalchoice1b
            
    label finalchoice1b:
        
    "...no, I know that's wrong now."
    
    jump finalchoice1
    
    label finalchoice1a:
        
    a "Even if you truly didn’t want to talk about it, I should’ve pushed you."
    
    a "Maybe, just maybe, taking it off your chest would’ve helped you understand your own feelings a little bit better."
    
    a "It would’ve also shown that I cared enough."
    
    hide carol happy with dissolve
    scene bg bedroom2 with dissolve
    show carol concerned with dissolve
    pause 2
    
    a "Then, when we were talking about the time I was in love with you…"
    
    a "...well, to be honest, I still was."
    
    a "Precisely because my love had not faded, precisely because I still cherished you as one would cherish a lover, I was scared to answer."
    
    c "What is it that you liked about me?"
    
    "I should've said..."
    
    jump finalchoice2
    
    label finalchoice2:
        
    menu:
        "“What I liked about you was...“":
            jump finalchoice2a
        
        "“It doesn't really matter...“":
            jump finalchoice2b
            
    label finalchoice2b:
        
    "But it did matter."
    
    "It mattered a lot."
    
    jump finalchoice2
    
    label finalchoice2a:
        
    a "Your smile, your determination, your relentless joy… and actually, far too many things to count."
    
    a "It would’ve been embarrassing to say, but it could’ve helped so that you’d see yourself in a better light."
    
    hide carol concerned with dissolve
    scene bg street2 with dissolve
    show carol concerned with dissolve
    pause 2
    
    a "Then you showed me your weak side, you shared your problems with me."
    
    a "Your career as a writer was on the line, and for the first time since I met you, you were confused and scared, because there was a wall that you couldn’t overcome."
    
    c "Really, I don't know what to do..."
    
    "I should've..."
    
    jump finalchoice3
    
    label finalchoice3:
        
    menu:
        "Encouraged her.":
            jump finalchoice3a
        
        "Stayed quiet.":
            jump finalchoice3b
            
    label finalchoice3b:
        
    "Saying anything at that time would’ve been better than saying nothing at all."
    
    jump finalchoice3
    
    label finalchoice3a:
        
        a "Just a small dose of support."
        
        a "That would’ve been enough… and yet I didn’t."
        
        hide carol concerned with dissolve
        scene bg building outside with dissolve
        show carol happy with dissolve
        pause 2
        
        a "Finally, it came that time, when you were troubled by something, but I didn’t dare to ask what."
        
        a "I made you extremely mad, remember? And in retrospect, I can understand why."
        
        a "You were probably trying to tell me about your plans to leave the city forever."
        
        a "You probably wanted to have a heart-to-heart with me, so that that you could depart knowing that our bond would never break."
        
        a "I confused your uncertainty with unwillingness to talk."
        
        "Still, what I should've done was..."
        
        jump finalchoice4
    
    label finalchoice4:
        
    menu:
        "To ask what was wrong.":
            jump finalchoice4a
        
        "To drop the subject.":
            jump finalchoice4b
            
    label finalchoice4b:
        
    "I don't want to make her angry again, do I?"
    
    jump finalchoice4
    
    label finalchoice4a:
        
    a "A sequence of small failures that in the end amounted to something big, something that couldn’t be taken back."
    
    a "Though to be honest, I’m not sure how much each of these choices really mattered."
    
    a "Maybe, just like that time at the bus station, they didn’t matter at all."
    
    hide carol happy with dissolve
    scene bg living room with dissolve
    stop music fadeout 1
    show carol blur with dissolve
    pause 1
    
    a "Still, I like to think they did... that they changed something in you."
    
    a "I don’t know."
    
    a "Maybe I just want to believe that my words were THAT important to you…"
    
    a "...as horrible as that might sound."
    
    "I rest my voice, and my eyes fall to the ground."
    
    "Guilt amounts in my heart."
    
    c "..."
    
    "I feel that the illusion is worried."
    
    "Maybe the guilt was too much for me to bear?"
    
    "Maybe her loss was too saddening?"
    
    "Maybe, just maybe, I was thinking about following her same path?"
    
    a "Don’t be ridiculous."
    
    "I stare back right at her."
    
    a "No, I won’t do such a thing."
    
    a "You not being here, and knowing that I’m partly responsible for that, hurts so much that it’s almost unbearable."
    
    a "Almost."
    
    hide carol blur with dissolve
    
    "I stand up."
    
    "I slowly walk forward, to the coffin."
    
    "It’s closed, so I can’t see her face, but even so I place my hands over the lid, and for a moment I believe I can feel what’s left of her warmth."
    
    a "Sure, it’s going to be hard, but I’ll keep going."
    
    a "I admired you, Carol. You took every hardship into your hands, and crushed them with all you had."
    
    a "It might’ve been only a front, a mask you used to deceive the world around you… but it was a mask I adored to watch nonetheless."
    
    a "I wanted to be like you, in some way or another."
    
    a "So I’ll try."
    
    a "It might be hard, but I’ll try."
    
    a "For myself… and for you as well."
    
    "I press my forehead against the place where I thought hers would be."
    
    "Tears fall to the wood."
    
    a "I think I know why you tried to kill yourself back then. I think I can piece it together now."
    
    a "It wasn’t because of your family, or Julian, or your writing, or anything of the sort."
    
    a "You just had a bad day, right?"
    
    a "For some reason, you woke up feeling like it was a bad day, the worst day imaginable."
    
    a "It happens… it happens to everyone."
    
    a "I’ve had too many bad days since you left the city, and I’ll keep having them now that you’re gone."
    
    a "But maybe it’s for the best."
    
    "I separate myself from her cage."
    
    "Soon she’ll be taken back to the depths of the earth, where she’ll finally be able to rest in peace, like she probably wanted."
    
    "I head to the door."
    
    "My hands touch the knob, cold as hell."
    
    "I turn my head around to face her body for the last time."
    
    a "Bye Carol."
    
    a "We had fun together."
    
    scene bg blackscreen with dissolve
    pause 3
    
    centered "...I'm glad I met you."
    
    play sound "door close.wav"
    pause 4

    return
