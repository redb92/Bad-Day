# Declare images below this line, using the image statement.
image bg bedroom = "bg bedroom.jpg"
image bg blackscreen = "bg blackscreen.jpg"
image bg bedroom2 = "bg bedroom2.jpe"
image bg street1 = "bg street.jpe"
image bg street2 = "bg street.jpe"
image bg building outside = "bg street.jpe"
image bg bus station = "bg bus station.jpe"
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
define k = Character ('Katherine', color="#FF8000")
define s1 = Character ('Stranger 1', color="#8904B1")
define s2 = Character ('Stranger 2', color="#8904B1")

define dissolve = Dissolve (.5)

# The game starts here.
label start:
    
    scene bg blackscreen
    
    pause 1

    "Is it realistic to feel like I’m special to others?"

    "Is it realistic to think I can make a difference in a friend’s life, that I can help them out in their times of need?"
    
    "Is it realistic to hope they’d lean on my shoulder and call my name if something bad were to happen?"
    
    pause 1
    
    c "I tried to kill myself last summer."
    
    pause 2
    
    "That day, for the first time, I began to doubt it was."
    
    pause 1
    
    scene bg bedroom with dissolve
    pause 1
    
    "She brought it up one afternoon like any other."
    
    play music "scene 1.mp3"
    pause 2.5
    
    "The season had only just begun, but leaves were already falling off their branches."
    
    "Sitting at opposite sides of a small table, me and my friend Carol, whom I hadn’t seen for a while, chatted, as usual."
    
    "It’s puzzling, because that’s the only thing I can remember from that day."
    
    "I can’t remember what made her bring it up, if there were any special circumstances surrounding our meeting, or anything of the sort."
    
    "I only know that at some point she said it:"

    show carol happy with dissolve
    pause .75
    
    c "I tried to kill myself last summer."
    
    "It took me by surprise; it shocked me, even."
    
    "How was I supposed to respond?"
    
    "Bewildered, I remained silent, giving Carol enough time to continue."
    
    show carol smile
    
    c "You look surprised."
    
    "She laughed nervously."
    
    show carol happy
    
    c "I don’t blame you: I can’t really believe it myself either."
    
    c "It’s a bit hard to explain..."
    
    "She smiled, but it seemed like a difficult topic to tackle, so she took a deep breath, preparing herself to talk."
    
    c "That night I had the sudden urge to take some pills, any pills I could find, and then swallow them whole as if nothing else mattered."

    c "Maybe it was my depression, trying to make some sort of big comeback? Who knows. Bottom line is that it happened."
    
    c "And it was weird."
    
    c "I hallucinated for the first time in my life. Some of it was scary, but some of it kinda exciting as well."
    
    show carol smile
    
    c "Looking back on it, I might have even had fun!"
    
    "I can’t see how’s that possible."
    
    show carol happy
    
    c "Of course, next morning I woke up in a hospital, dizzy, unable to remember most of what happened the other night."
    
    c "I told my parents what I had done..."
    
    show carol troubled
    
    c "...and as expected, they didn’t take it too well."
    
    c "The doctors advised me to take it easy but that I’d be able to leave soon, because contrary to my expectations, the pills hadn’t done anything weird to my body."
    
    show carol happy
    
    c "...guess I should’ve gone with a shotgun instead, huh?"
    
    show carol smile
    pause 1
    show carol troubled
    pause 1
    
    "She laughed, but stopped after looking at my face. My expression must’ve been grim."
    
    show carol happy
    
    c "...anyway, I got discharged a few days after."
    
    show carol happy
    
    c "Things went back to normal pretty quick: I visited my cousins, spent some days at the beach, had some fun with Julian and his friends…"
       
    c "But when the time came for me to come back, my parents refused to let me go."
    
    show carol troubled
    
    c "It wasn’t hard to see why. Their only daughter tried to kill herself! Of course they’d react the way they did."
    
    c "Why can’t you attend a school from around here?’ they said."
    
    show carol happy
    
    c "In the end, I promised to visit a psychiatrist at least once a week, to give them some peace of mind."
    
    show carol angry
    
    c "It doesn’t stop them from calling every day to check if I’m still at it."
    
    a "Are you?"
    
    show carol happy
    
    c "Yes."
    
    c "It sucks, but I am."
    
    c "I’m also on pills. That’s really all what going to the doctor is good for: pills, loads of pills, so that I never feel like killing myself again."
    
    show carol smile
    
    c "It’s all pretty ironic when you think about it."
    
    "Again, I couldn’t bring myself to laugh. I just listened in silence, as it always was whenever we met to talk."
    
    show carol happy
    
    c "That’s all there is, Alan. I’ve summed up my adventures as best as I could."
    
    show carol smile
    
    c "Don’t tell a soul, alright? Not a lot of people know about this... and I want it to remain that way."
    
    show carol happy
    
    "I carefully chose my words."
    
    a "Who else have you told?"
    
    "She counts with her fingers."
    
    c "My family, Julian, a couple of friends from back home… that’s about it."
    
    "It wasn’t something that you would tell just anyone, so it made sense that she’d want to keep it among close friends and family."
    
    hide carol happy with dissolve
    
    "It made sense… but then again, if that day she hadn’t chosen to tell me, would I have known about it eventually, or would I have been kept in the dark, blissfully unaware of my friend’s suffering?"
    
    "‘Why did you do it?’ I wanted to ask, but the words got caught up in my throat, they refused to let go, they were afraid she might have not responded, thus proving that I wasn’t trustworthy enough in her eyes."
    
    show carol troubled with dissolve
    
    c "I’m not sure why I did it."
    
    "But she tried to answer anyways."
    
    c "I’ve got good grades, right? And Julian is still by my side. Honestly, there wasn’t anything wrong with my life."
    
    c "But that morning, when I looked myself in the mirror, I just felt… it was all just so…"
    
    c "..."
    
    show carol happy
    
    
    c "…no, you don’t want to hear it."
    
    "But I do."
    
    "So I really should say..."
    
    menu:
        "'You probably don't want to talk about it.'":
            jump choice1
            
    label choice1:
        
    a "You probably don’t want to talk about it."
    
    "Don’t say that, Alan."
    
    c "No… I really don’t."
    
    "Don’t let her say that, Alan."
    
    a "Then that’s alright. I’ve heard enough."
    
    "‘Tell me once you feel ready’, I forgot to add."
    
    show carol smile
    
    c "Yeah, thanks for putting up with me!"
    
    show carol happy
    
    a "Don’t worry about it. We’re friends after all. Gotta look out for each other."
    
    show carol smile
    
    c "Damn right! And don’t worry: I’m not planning to do it again. It was, you know, just a bad day."
    
    show carol happy
    
    c "For no reason at all, I woke up feeling like it was the worst day imaginable…"
    
    show carol smile
    
    c "We all have mornings like that, right?"
    
    hide carol smile with dissolve     
    
    "It was a clear day, just like every other early autumn day."
    
    "We chatted on her apartment’s terrace, just like every Friday afternoon."
    
    "Every Friday, because it was only on Fridays that neither of us had to attend college."
    
    "On her terrace, because we were neighbors, and her place was always tidier than mine."
    
    "Every day we’d wake up at roughly the same time, eat breakfast, and then step out of our apartments to meet in the corridor outside."
    
    "We’d walk the 20 minutes that separated us from the local college, making small talk on the way, going our separate ways upon reaching the main gates."
    
    "Two years, always the same routine."
    
    "I had gotten used to her, and she had gotten used to me. It was only natural that our incidental friendship would grow into something else."
    
    "Though by that I don’t mean anything romantic."
    
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
    
    hide carol angry with dissolve
    
    "Julian was Carol’s boyfriend."
    
    "A nice fellow, though we never talked much. He was a violinist trying his best to survive in the ruthless world of classical music."
    
    "From what I know, Carol and Julian had known each other since they were little, and started dating while in high school."
    
    "They decided to move in together to the big city a year after graduating, as education back in their hometown wasn’t enough for their grander goals."
    
    show carol angry with dissolve
    
    a "Really, you just can’t make a living out of music, or any type of art, for that matter."
    
    "I said, trying to be mean on purpose."
    
    c "Hmph, now you’re just being an asshole!"
    
    "Incidentally, Carol was a writer; a struggling poet of sorts."
    
    show carol happy
    
    c "I’ll get a book published one day, just you see."
    
    a "Sure, break a leg."
    
    show carol troubled
    
    c "Take me seriously for once, alright?"
    
    c "You know it's something important to me."
    
    a "...Alright. You can do it. I mean it."
    
    "But she didn’t take my word for it and just looked away."
    
    "I knew she was faking her sadness for the most part, but it still made me regret my words."
    
    "I considered my options, wondering what would be the best way to cheer her up."
    
    a "Wanna go eat some donuts?"
    
    c "..."
    
    a "How about a public reading? You like those, don’t you?"
    
    c "..."
    
    a "..."
    
    hide carol troubled with dissolve
    
    "Despite my best efforts, I wasn’t getting anywhere."
    
    "I looked around the room, searching for something that could help me break the awkwardness."
    
    show carol troubled with dissolve
    
    a "…t-this place is awfully messy today."
    
    show carol angry
    
    c "I know, right?!"
    
    "Carol suddenly jumped up from her seat."
    
    c "Julian just threw his clothes everywhere and left a huge-ass mess on the kitchen last night! And I’ve barely had any time to clean!"
    
    c "Why should I clean anyway? It’s his mess! Julian should be the one to clean!"
    
    a "Sounds fair."
    
    c "Also, last night, after cooking? He just went to sleep, without even giving me a kiss! I feel unloved, man."
    
    c "Plus I was finally in the mood for some-"
    
    pause 1.5
    
    "She putted a stop to her words."
    
    a "I understand. Still, he was probably very tired."
    
    c "I know he’s tired! He’s always tired! It’s the worst! And I gotta be here, and clean after him, and with school and all it’s just too much!"
    
    c "..."
    
    show carol happy
    
    c "Well, I suppose I can forgive him for once."
    
    "Getting her to complain about Julian was always a good way to lift her spirits."
    
    "As with every relationship, theirs’ had its ups and downs, but I knew that deep down they loved each other: she was always going to put up with his mess, and he was always going to put up with her complaints."
    
    "I was jealous, in more than one way."
    
    hide carol happy with dissolve
    pause 1.25
    
    "…and that’s how it usually went. We just talked: about our lives, about the people in our lives, about the lives of the people in our lives."
    
    "It was a Friday afternoon just like always, except…"
    
    c "'I tried to kill myself.’"
    
    "I’m sure she didn’t want me to dwell on it; I’m sure she wanted me to act like always, to not let it weigh on my soul."
    
    c "‘I tried to kill myself last summer’."
    
    "But I couldn't."
    
    "I couldn't."
    
    "I couldn't get that out of my head."
    
    "Whenever I thought back on it, whenever I tried to find an explanation, my heart just fell into a spiral of confusion and contempt."
    
    "Carol was one of the brightest people I had the luck to meet."
    
    "She greeted the day with a smile, she worked with a smile, and whenever things got tough, she brushed it off and worked twice as hard to overcome it."
    
    "I just couldn’t imagine her with dozens of pills down her throat."
    
    "I couldn’t imagine her with the drive to end her own life."
    
    "But she did, she told me so, unless she was lying, which made no sense."
    
    "I couldn’t understand her, and that bothered me. That she never told me about her depression bothered me even more."
    
    scene bg blackscreen with dissolve
    pause 1.5
    
    "However, the absolute worst part was how, for roughly 3 months, I never knew about any of this happening."
    
    "How she never called me, not even to say hi, during the entirety of that summer."
    
    scene bg bedroom with dissolve
    show carol happy
    pause 1
    
    c "Something wrong, Alan?"
    
    a "…no, nothing’s wrong."
    
    "I lied, shamelessly."
    
    hide carol happy with dissolve
    scene bg blackscreen with dissolve
    stop music fadeout 1
    pause 3
    
    "Carol’s issue occupied my mind for the next couple of weeks."
    
    "I was worried, but at the same time, trying to fix an unsolvable problem wasn’t going to be of any use, so I composed myself as best as I could."
    
    scene bg bedroom2 with dissolve
    pause 1
    
    "Besides, I had my own problems to deal with."
    
    "Dating is a complicated thing, after all."
    
    play sound "cell vibrate.wav"
    pause 1.5
    queue sound "cell vibrate.wav"
    pause 2
    play sound "beep.wav"
    pause 1.5
    
    k "I think we should break up."
    
    "It all came falling down on me with a single phone call from my then-girlfriend, Katherine."
    
    "As I let those words sink in, I realized they didn’t hurt me as much as I thought they would."
    
    a "I understand."
    
    k "..."
    
    a "..."
    
    a "Kate?"
    
    k "Is that all you’re going to say?"
    
    "My complacency must’ve rubbed her the wrong way."
    
    a "No, I was giving the idea some thought as well."
    
    a "We barely see each other nowadays: I’m busy studying, you’re busy with your job and besides…"
    
    k "…we’re not as into it as we used to be, right?"
    
    a "You read my mind."
    
    "She sighed, possibly in relief."
    
    k "Honestly, I’m glad you feel the same way."
    
    "Of course, I had no way of knowing if she was telling the truth."
    
    a "Like this, no one gets hurt."
    
    k "Yeah…"
    
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
    
    play sound "beep.wav"
    pause 1
    
    "Kate hung up."
    
    "Just like that, a relationship of eight months came to an end."
    
    pause 1
    play music "scene 2.mp3"
    pause 2.5
    
    a "It's finally over, huh..."
    
    "I contemplated the screen of my phone in a daze, all while thinking about my time spent with Kate."
    
    "If someone were to ask me if being with her made me unhappy, I’d say not really."
    
    "It simply didn’t make me happy enough."
    
    "At some point, we became more friends than lovers, and then simply casual friends that were too scared to hurt each other by breaking up."
    
    "Kate was brave enough to take that final step."
    
    "I wasn’t."
    
    "Somewhere inside, I was jealous of her bravery."
    
    "Still, eight months… that’s a long time. Enough time to get attached to someone."
    
    "I wondered if she was truly alright with breaking up. I wondered if she didn’t do it just to make things easier on me."
    
    "It was something I couldn’t ask, something that I’d never know."
    
    play sound "cell vibrate.wav"
    pause 1.5
    queue sound "cell vibrate.wav"
    pause 1.5    
    
    "My phone rang again. Was it Kate?"
    
    a "..."
    
    "No, it was Carol."
    
    "I quickly picked it up."
    
    play sound "beep.wav"
    pause 1
        
    c "Hey buddy!"
    
    c "Do you have any time to spare?"
    
    a "Do YOU have any time to spare? Aren’t you supposed to be in class now?"
    
    c "Listen to this! Our teacher didn’t show up, and he didn’t even send an email to warn us! So I’m at home now, watching some TV."
    
    c "So? Wanna go have a drink with an old friend?"
    
    a "…Nah, I don’t really feel like it."
    
    c "Why? What’s wrong?"
    
    a "I just broke up with Kate… so you know, not a great time."
    
    stop music fadeout 1
    pause 1.5
    
    c "..."
    
    play sound "beep.wav"
    pause 1
    
    play sound "thump.wav"
    pause 1.5
    
    "I felt something heavy fall to the floor somewhere in the building as Carol hung up."
    
    pause 1.25
    
    play sound "knocking door.wav"
    pause 2
    
    "Moments later, a pair of fists furiously knocked against my door."
    
    scene bg blackscreen with dissolve
    
    "Slowly, methodically, I unlocked the door to let Carol in."
    
    play sound "unlock door.wav"
    pause 2.2
    
    show carol angry at left with dissolve
    
    c "What?! Why?! How?!"
    
    hide carol angry
    
    show carol angry with dissolve
    
    c "Just what did you do Alan?!"
    
    a "Calm down. I didn’t do anything."
    
    c "But you looked so cute together! And she was such a sweet girl! Just why would…?!"
    
    "She was so out of breath that she couldn’t even finish her words."
    
    a "I’ll get you some water."
    
    hide carol angry with dissolve
    scene bg bedroom2 with dissolve
    pause 1
    play music "scene 2.mp3"
    pause 2
    
    "We moved to my room a few moments later, and Carol thankfully got a grip on herself by then."
    
    show carol angry with dissolve
    
    c "So? Please explain."
    
    show carol neutral
    
    "I tried to explain myself: how I didn’t feel particularly happy being in a relationship, how we barely had time to see each other, how in the end Kate ceased to feel like a lover to me."
    
    "Carol listened to me in silence, nodding every once in awhile."
    
    c "I see."
    
    show carol happy
       
    c "Well, if that’s how it was, then it’s only logical to break up… but it feels like a waste."
    
    a "How so?"
    
    c "You looked good together, and you seemed to understand each other very well."
    
    show carol smile
    
    c "I kinda hoped to see you guys getting married one day."
    
    show carol happy
    
    "Her words perplexed me."
    
    "Me? Married with Kate?"
    
    "I tried to picture the scene, she and I sharing a home, raising a family, living as husband and wife, but I couldn’t: it felt too surreal to imagine."
    
    a "The thought never crossed my mind."
    
    show carol concerned
    
    c "Really? Not even once?"
    
    a "No. Or at least, not that I remember. Maybe I imagined it once, back when we started, but now it feels so distant that I can’t be sure."
    
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
    
    a "Wait, Carol, just how often do you speak with Kate?"
    
    show carol happy    
    
    c "Once a week, I guess."
    
    "That was a legitimate surprise."
    
    a "…I didn’t know you were that close. I thought you only saw each other when she visited."
    
    c "It used to be that way, but she added me on Facebook a few months ago and we’ve been hitting it off ever since."
    
    a "I see. I wasn’t expecting that."
    
    c "In fact, she told me quite a few things I didn’t know about you. Wanna know what?"
    
    a "...no, I really don’t want to ask."
    
    show carol smile
    
    c "Wise choice!"
    
    show carol happy
    
    "I took a deep breath."
    
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
    
    c "Ahh, damn… you looked so good together. Such a waste… such a waste…"
    
    hide carol concerned with dissolve
    
    "Carol mumbled the same thing over and over, but she eventually stopped to set her gaze across the window."
    
    "It was a gray day outside. Dark clouds covered the sky, threatening to fill the entirety of this town with endless rain."
    
    "Had I ever truly fallen in love with someone until then?"
    
    "I tried to look back to my elementary school days, to my high school days, up to the current date, but I could only remember one time that I was truly ‘in love’."
    
    show carol happy with dissolve
    
    a "You know… back when we first started hanging out? I was kinda in love with you."
    
    stop music fadeout 1
    
    c "..."
    
    c "Eh?"
    
    a "Back when we were freshmen I was in love with you. Like, seriously in love."
    
    "For a moment, Carol became unable to respond, my sudden confession overwhelming all of her senses."
    
    "Little by little her cheeks took a reddish color, and so did her ears."
    
    "She tried to say something, anything, but nothing came out of her mouth."
    
    a "...are you ok?"
    
    show carol smile with dissolve
    pause .7
    show carol happy with dissolve
    
    c "Eh?! Y-yeah, of course I’m okay."
    
    c "But damn..."
    
    c "You really don’t know how to pull your punches, huh?"
    
    hide carol happy with dissolve
    
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
    
    "I looked away with a bunch of conflicted feeling climbing up my back."
    
    show carol smile
    
    c "What is it that you liked about me?"
    
    show carol happy
    
    "She spitted out a question I didn’t want to answer."
    
    a "It was too long ago, so I can’t remember."
    
    "I did my best to dodge the bullet."
    
    show carol angry
    
    c "Can’t you make an effort?"
    
    "Carol wouldn’t drop it. She moved closer, enough to make me crawl back on my seat."
    
    "My words weren’t supposed to hold any special meaning, so why was she acting like that? What did she want?"
    
    a "..."
    
    show carol concerned
    
    c "Alan?"
    
    "She was pressing me for an answer."
    
    "What should I have said?"
    
    menu:
        "'It doesn't really matter...'":
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
    
    hide carol smile with dissolve    
    
    show carol concerned with dissolve
    
    "I stood up from my seat. I didn’t walk up to her, I didn’t even look at her, I just stood up, enough to emphasize my growing anger."
    
    "A heavy silence engulfed the room."
    
    "Carol looked surprised, possibly even scared."
    
    "I should’ve apologized then, but my mind wasn’t composed enough to do it."
    
    "Or rather, I didn’t want to do it."
    
    pause 2
    
    "Neither of us spoke for what felt like hours."
    
    pause 2
    
    c "I’m sorry. I shouldn’t have pushed you."
    
    "Her voice sounded hoarse."
    
    c "You have every right to be angry. Like, you broke up with your girlfriend just a second ago! Of course you’re angry!"
   
    show carol happy
   
    c "Really, just how self-centered can I get?"
    
    "Every word she said filled me with guilt."
    
    c "I-I know! Wanna eat something? Drink? Maybe… watch a movie?"
    
    show carol concerned
    
    c "…Alan?"
    
    "But other than looking up, I said nothing in response."
    
    show carol happy
    
    c "…ok, you’re not in the mood. I understand. Then, do you need anything? Do you want to be left alone?"
    
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
    
    show carol smile
    
    c "Well then… see you later."
    
    a "Wait..."
    
    hide carol smile with dissolve
    
    "‘I’m sorry’. Was that the right thing to say?"
    
    "‘It’s not your fault’. Was that the right thing to say?"
    
    "‘Let’s forget we ever talked about this.’ Was that the right thing to say?"
    
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
    
    play sound "streetsound.wav"
    pause 10
    
    "Taking a walk across the neighboring shopping district, I glanced at a peculiar sight."
    
    "A block away from me, in front of a trendy café, I recognized Carol talking with two other guys I didn’t know."
    
    a "...classmates, maybe?"
    
    "It was a rare occurrence to meet Carol outside our school campus, let alone see her in this part of town."
    
    "As friendly as she may have been, her days consisted mostly of going back and forth between her apartment and school."
    
    "Honestly, it never felt like she liked people too much, but I assumed it was only my imagination."
    
    "A large crowd separated us and I could barely keep her in my sight."
    
    pause 1
    
    "(Couldn't find good steps audio)"
    
    "Little by little I tried to make my way across the street, careful not to run into anybody along the way."
    
    pause 1
    
    "(Couldn't find good steps audio)"
    
    "As I got closer, however, I realized something was wrong with Carol and the two young men."
    
    "It was difficult to distinguish from where I stood, but they seemed to be, if not fighting, at least having a heated argument."
    
    "Carol shouted something to one of the strangers, but the crowd mitigated the sound."
    
    "The stranger remained calm, but he was clearly reaching the end of his patience."
    
    "His partner (or assumed partner) stood a few feet away, unwilling to join the conversation."
    
    "It didn’t look good. Carol kept arguing, oblivious to how the stranger’s expression was gradually getting more and more tense with each passing second."
    
    "Seeing no other choice, I prepared myself to step in."
    
    show carol angry at right with dissolve
    pause 0.8
    
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
    
    hide carol angry at right with dissolve
    
    show carol angry with dissolve
    
    a "..."
    
    c "..."
    
    "Carol’s expression looked sour, and I was afraid of asking for a reason."
    
    pause 1
    
    show carol happy with dissolve
    
    pause 1
    
    play music "scene 3.mp3"
    pause 1
    
    c "Thanks for helping me out: a few more seconds and I would’ve exploded on the guy."
    
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
    
    c "I needed to vent somehow."
    
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
    
    "I had read some of her stuff, but I had never been able to understand it. Metaphors were too foreign to the simple words and meanings I was used to."
    
    "Of course, even if we didn’t understand each other, we were still friends. Friends don’t need to have dreams in common, or anything in common, to get along."
    
    "However, from time to time, I felt knowing so little about Carol, Carol the Writer, was a mistake."
    
    "That I should’ve tried to understand her better or else our lives would have eventually drifted away."
    
    "Such thoughts scared the crap out of me."
    
    a "Do you not get along with those guys?"
    
    "I decided to ask after a few minutes of silence."
    
    show carol neutral with dissolve
    
    c "...not really. Oh, but I don’t hate them or anything! I just don’t... “like” them either. They are OK people, just not people I’d be friends with."
    
    show carol happy
    
    c "Does that make any sense?"
    
    a "It makes perfect sense. But if that’s the case..."
    
    c "You want to know why we were fighting, right? It's so easy to tell."
    
    show carol smile
    
    c "C’mon Alan, we’re buddies, right? You should ask whenever you feel like asking, otherwise you’ll hurt my feelings."
    
    show carol happy
    
    a "Alright then. Why were you fighting?"
    
    c "Pride, mostly. Artists are prideful people: we’ll butt heads whenever someone talks shit about our work."
    
    show carol angry
    
    c "You see, the writing workshop I go to is “harsh”."
    
    show carol happy
    
    c "Every week, our teacher asks us to hand over everything we’ve written over the past few days, be them short stories or poems, regardless of whether we’ve finished them or not."
    
    c "We take turns to read our writing out loud, and then everyone shares their opinion on the text."
    
    c "Some might say it was good, some might say it was bad. Our teacher values constructive criticism over the typical “I liked it” or “I hated it”."
    
    a "It sounds like a good system."
    
    show carol smile
    
    c "It usually is."
    
    show carol happy
    
    c "However, when opinions are too divisive, it can turn our workshop into an all-out war."
    
    show carol concerned
    
    c "...Some of us are especially sensitive when our writing is criticized."
    
    show carol neutral
    
    c "Me and the angry guy from before, we always “fight” on opposite sides, so now there’s some sort of rivalry between us."
    
    c "As I said, I don’t hate him, and he doesn’t hate me either. At least, I hope so... but sometimes things can get out of control."
    
    show carol angry
    
    c "...especially when you just know you’re in the right!"
    
    a "Did he… I don’t know, say something bad about a poem of yours?"
    
    show  carol concerned
    
    c "It’s a bit more difficult than that."
    
    show carol happy
    
    c "You see, today our teacher walked in with some pretty exciting news: we were all going to contribute to an anthology where we’d be able to showcase one of our better works."
    
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
    
    "There were a few parts that confused me, however."
    
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
    
    "Really, I don’t know what to do..."
    
    show carol concerned
    
    "I should’ve said something, anything."
    
    menu:
        "Stay quiet":
            jump choice3
            
    label choice3:
    
    "But yet again, with my sight set on the ground, I remained silent, without changing a single thing."
    
    c "Maybe I could just compromise."
    
    "Carol didn’t seem pleased at the thought."
    
    "As long as I’m published, I really don’t mind making a few sacrifices."
    
    "But she minded, a lot. It was crystal clear by the way she talked."
    
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
    
    "Carol was a cheerful and friendly person, someone who could make you open up to her in the brink of an instant."
    
    "It was difficult for me to imagine her as a person with few friends."
    
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
    
    scene bg blackscreen with dissolve
    play sound "unlock door.wav"
    pause 1
    play sound "door close.wav"
    pause 1
    
    
    "By this time of the year, students begin to wish for their share of solitude, as if consumed by the freezing atmosphere in the air."
    
    "Winter equals exams, after all. Loads of them. Enough to fill your head with worries over whether or not your grades are good enough to save the semester, stress oozing from every inch of your body."
    
    "Needless to say, I was going through such a predicament. And so was Carol."
    
    "The both of us had locked ourselves in our apartments, willing to spend days, if not weeks, reviewing our respective material and finishing assignments due the following mornings."
    
    "Irregular schedules and a duty to keep studying, no matter the circumstances, had decreased the number of times we met every week."
    
    "We texted each other, exchanging small jokes to make the studying a little more bearable, but we didn’t see each other nearly as much."
    
    "I didn’t hear her voice for over 2 weeks."
    
    "It might sound strange, considering we were neighbors, but there was really nothing weird about it."
    
    "Carol was the type of person who wouldn’t stop studying until her exams were over."
    
    scene bg building outside with dissolve
    
    "Me, well… I was never an exemplary student: I did what I had to do and nothing more than that."
    
    "But seeing Carol put so much effort into it made me want to try a little bit harder myself."
    
    "Besides, I didn’t want to distract her in such a crucial time."
    
    "Something did catch my attention: after our conversation from a few months back, she had never again mentioned anything related to the compilation."
    
    c "“I’m working on a few poems right now.”"
    
    c "“I believe this is turning out good.”"
    
    "I’d hear small comments such as these, but never anything concrete."
    
    "Sometimes I found myself thinking about it."
    
    "‘Maybe I should call and ask.’"
    
    "‘...but if she doesn’t want to tell me, then I can’t force her.’"
    
    "‘What if she does want to tell me?’"
    
    "‘No. If she did, she would’ve told me herself.’"
    
    "I’d often have this conversation with myself, and I’d always reach the same resolution."
    
    "I thought I wouldn’t hear from Carol again until after she was done with her exams."
    
    "That is, until I got a call from her."
    
    play sound "cell vibrate.wav"
    pause 1.5
    queue sound "cell vibrate.wav"
    pause 2
    play sound "beep.wav"
    pause 1.5
    
    c "‘Sup dude! How’s it going?"
    
    a "Alright, I guess. I just stepped out for a bit to get some fresh air."
    
    c "Yeah, I see you from up here. Isn’t it freezing?"
    
    a "Not so much."
    
    c "Do you have some time to hang out? If so, I’m coming down."
    
    a "Sure. I’ll wait for you by the door."
    
    play sound "beep.wav"
    pause 1.5
    
    "Moments later, Carol stepped out of the building, sweating in some unnatural way."
    
    show carol smile with dissolve
    
    a "Did you just run down the stairs?"
    
    show carol angry
    
    c "The elevator was taking way too long!"
    
    a "You’re going to get a cold that way, with this weather."
    
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
    
    a "Let’s hope that’s the case. I’ve been trying… and for real, this time. Not like last year."
    
    "Carol nodded in agreement."
    
    show carol smile
    
    c "Yup, I know. You’ve grown so much!"
    
    show carol happy
    
    "She proceeded to mess with my hair."
    
    "It was a bit awkward because of our height difference, but somehow she stretched enough to reach my head with the tips of her fingers."
    
    "She was trying to make fun of me, but her touch felt so tender that I just let her do what she wanted."
    
    "Carol stayed like that, on her tiptoes, for a while that felt like an eternity."
    
    hide carol happy with dissolve
    show carol blush with dissolve
    pause 1.5
    hide carol blush with dissolve
    show carol concerned with dissolve
    
    "It doesn’t take me long to feel that something’s wrong."
    
    a "Carol? Are you ok?"
    
    show carol happy
    
    c "I’m doing just fine."
    
    "And in saying so, she stepped away from me, looking just like always."
    
    "Was it my imagination?"
    
    show carol smile
    
    c "Maaaan, it’s been ages since I last went outside! It’s nice feeling the air on my cheeks again, even if it’s cold as fuck."
    
    "Have you been locked in your apartment all this time? That’s not very good for you."
    
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
    
    c "...not really. Just a bit of fighting going on the side. Same as usual. Nothing you should worry about."
    
    "Carol put her hands together and timidly played with her fingers."
    
    "It seemed she had something to say, but didn’t know how to put it into words."
    
    "It was somewhat worrying."
    
    a "Did he hit your or something?"
    
    show carol angry
    
    c "N-no! What would make you think that? You know that Julian would never dare put a finger on me!"
    
    a "O-ok, I’m sorry."
    
    "She seemed genuinely angry at my suggestion, so she must’ve been telling the truth."
    
    show carol happy
    
    "There was something wrong with her, but asking didn’t feel right, and I didn’t believe Carol would feel comfortable sharing it with anyone."
    
    "Even if it was me."
    
    menu:
        "Drop the subject":
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
    
    c "‘I won’t ask’, ‘I’ll drop the subject’, ‘let’s talk about something else.’"
    
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
    
    a "No, it’s ok. I’m pretty much at fault on this one. Or maybe no one is at fault. Yeah, let’s go with that."
    
    show carol smile
    pause 1
    
    "She laughed, looking a bit more relaxed."
    
    a "Still, I’ll keep your words in mind."
    
    show carol neutral
    
    a "It was somewhat flattering to hear you say that I’m a kind person. No one has ever said that to me before."
    
    show carol smile
    
    c "It was quite embarrassing to say! I’m not going to repeat it, ok?"
    
    show carol happy
    
    c "And don’t forget about the important part of our conversation."
    
    a "I won't ma'am."
    
    show carol smile
    
    c "Excellent."
    
    hide carol smile with dissolve
    
    stop music fadeout 1
    
    scene bg blackscreen with dissolve
    
    "We decided to go back inside shortly afterwards. We took the elevator; the closed space warmed us up."
    
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
    pause 1
    
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
    
    c "He said that his father was sick, and that he wouldn’t be able to take care of Julian’s mother anymore."
    
    show carol concerned
    
    c "He’d been thinking about it for a long time, apparently."
    
    c "Julian practiced, and practiced, but never felt the same passion for music as he once did."
    
    c "Studying at that school, competing for rewards he didn’t desire…"
    
    show carol neutral
    
    c "He was making himself unhappier with each passing day."
    
    c "And I noticed as well, how lately he hadn’t been acting as himself."
    
    show carol happy
    
    c "And well… even though he told me I could stay, I decided to stay by his side."
    
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
    
    c "Just you see."
    
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
    
    show carol happy at right with dissolve
    pause 2
    
    "Carol smiled, just like she always did."
    
    "She never ceased to smile, even as she told me about all the problems she’d had."
    
    "I had too many questions I wanted to ask.. Why did she never tell me anything about this? Wasn’t there a way to convince Julian to stay? Couldn’t she stay, even if Julian wasn’t by her side?"
    
    "Why wouldn’t she trust me with her problems, with her secrets, with her company?"
    
    "But as always, I remained silent."
    
    hide carol happy at right with dissolve
    
    "The air in the station was cold, but leaning on each other’s shoulders as we waited for Carol’s bus to arrive made the experience a little more bearable."
    
    show carol happy with dissolve
    
    a "Do you have everything you need?"
    
    c "Mhm."
    
    a "Did you sort everything out with the landlord?"
    
    c "Yup, everything's ok."
    
    a "You sure you're not forgetting anything, right?"
    
    show carol angry
    
    c "Jesus Alan, stop acting like my mom!"
    
    c "Everything's fine, seriously."
    
    a "Sorry, sorry. I'm just..."
    
    hide carol angry with dissolve
    show carol happy with dissolve
    
    "I couldn’t explain my exasperation, but Carol seemed to understand regardless."
    
    "Buses came and went, people stepped in and out, and we waited, sharing our body heat as our only means of communication."
    
    show carol smile
    
    c "There it is."
    
    hide carol smile with dissolve
    
    "Carol stood up. At the same time, the speakers called for anyone heading towards Carol’s hometown: their transport was ready."
    
    "Defeated, I followed Carol to the platform."
    
    "People were loading their luggage and showing their tickets."
    
    "Carol did the same, handing over the few bags she was carrying."
    
    show carol happy with dissolve
    
    c "I guess this is it then."
    
    "My heart sunk, and I was unable to look her in the eye."
    
    show carol concerned
    
    c "Hey, c’mon. Don’t look so sad Alan; you’re going to make it hard for me as well."
    
    a "Yeah, I know. You’re that type of person after all."
    
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
    
    "Though that hug should’ve been enough, I quickly realized there was something else I wanted to say."
    
    a "Carol!"
    
    show carol neutral with dissolve
    
    "She stopped under the threshold, and turned around to face me."
    
    "Honestly, it was scary to say it. It was one of the countless things I’d held back over the past 2 years."
    
    "The thought of spouting those words and possibly changing something between us was scarier than anything I could ever imagine."
    
    "However, she explained herself well enough: how she hated whenever I avoided saying the things I wanted to say."
    
    "So I said..."
    
    menu:
        "'Take care of yourself.'":
            jump choice5a
        "'I love you.'":
            jump choice5b
    
    label choice5a:
        
    a "Take care of yourself."
        
    "Somehow, I managed to stop myself from saying something I shouldn’t."
        
    show carol smile
    pause 1.5
        
    c "...yeah, you take care as well."
        
    hide carol happy with dissolve
        
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
        
    a "I love you."
        
    "Though the words have a hard time crawling out of my throat, I somehow expressed the feelings I wanted to convey the most."
        
    hide carol neutral with dissolve
    show carol blush with dissolve
    pause 1.5
        
    c "Yeah."
        
    hide carol blush with dissolve
        
    "She hopped out of the bus, to the annoyance of the driver, who just wanted to leave the station at once."
        
    "It was for a brief moment, but I felt her cold lips rubbing against my left cheek."
        
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
    pause 1.5
    
    "We stayed in contact with each other via texting and occasional phone calls."
        
     
    
    
    
    return
