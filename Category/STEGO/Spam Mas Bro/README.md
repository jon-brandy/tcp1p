# Spam Mas Bro
> Write-up author: vreshco
## DESCRIPTION:
Saat saya membuka hp tiba-tiba ada seseorang yang mengirim ku pesan dan pesan nya ialah TCP1P, 
setelah dia mengirim pesan lalu dia mengirim lagi tetapi pesan nya ini sangat aneh dan bisa di 
katakan dia ini me-spam saya karena pesannya sangat banyak dan aneh, bantu aku mencari tahu apa arti pesan ini!!!

## HINT:
1. Spam Mimic adalah teknik penyandian pesan dengan menggunakan kumpulan kalimat acak yang dihasilkan secara otomatis dan menempatkan pesan asli di antara kalimat-kalimat tersebut untuk menyembunyikan pesan asli dari deteksi spam. Oleh karena itu, situs web Spam Mimic ini menawarkan layanan untuk memecahkan kode pesan yang telah dienkripsi dengan teknik ini.

## STEPS:
1. Given a `.txt` file.

> WITHIN

```
Dear Cybercitizen , This letter was specially selected 
to be sent to you . This is a one time mailing there 
is no need to request removal if you won't want any 
more ! This mail is being sent in compliance with Senate 
bill 1618 , Title 9 ; Section 304 ! This is NOT unsolicited 
bulk mail ! Why work for somebody else when you can 
become rich within 35 DAYS ! Have you ever noticed 
people are much more likely to BUY with a credit card 
than cash and nearly every commercial on television 
has a .com on in it ! Well, now is your chance to capitalize 
on this ! WE will help YOU use credit cards on your 
website and sell more . You can begin at absolutely 
no cost to you . But don't believe us . Mrs Jones who 
resides in Missouri tried us and says "Now I'm rich, 
Rich, RICH" ! We assure you that we operate within 
all applicable laws . Do not go to sleep without ordering 
. Sign up a friend and you'll get a discount of 90% 
. Thank-you for your serious consideration of our offer 
! Dear Salaryman ; Especially for you - this hot announcement 
. This is a one time mailing there is no need to request 
removal if you won't want any more . This mail is being 
sent in compliance with Senate bill 2516 ; Title 2 
; Section 306 ! This is a ligitimate business proposal 
! Why work for somebody else when you can become rich 
inside 48 days . Have you ever noticed most everyone 
has a cellphone & more people than ever are surfing 
the web ! Well, now is your chance to capitalize on 
this . WE will help YOU decrease perceived waiting 
time by 150% & increase customer response by 120% . 
The best thing about our system is that it is absolutely 
risk free for you . But don't believe us . Ms Ames 
who resides in Missouri tried us and says "I've been 
poor and I've been rich - rich is better" ! This offer 
is 100% legal ! For the sake of your family order now 
! Sign up a friend and your friend will be rich too 
. Warmest regards ! Dear Cybercitizen , This letter 
was specially selected to be sent to you . We will 
comply with all removal requests . This mail is being 
sent in compliance with Senate bill 2416 ; Title 7 
, Section 304 . THIS IS NOT MULTI-LEVEL MARKETING . 
Why work for somebody else when you can become rich 
inside 69 days ! Have you ever noticed the baby boomers 
are more demanding than their parents plus nobody is 
getting any younger ! Well, now is your chance to capitalize 
on this . WE will help YOU decrease perceived waiting 
time by 180% and SELL MORE ! You can begin at absolutely 
no cost to you . But don't believe us ! Mrs Anderson 
of Alabama tried us and says "Now I'm rich, Rich, RICH" 
. We are licensed to operate in all states ! Don't 
delay - order today ! Sign up a friend and your friend 
will be rich too ! Thank-you for your serious consideration 
of our offer ! 

```


2. Based from the challenge's title and it's hint, seems the message is encrypted with **spam encryption**.
3. We can decode that using [this](https://www.spammimic.com/decode.cgi) online tool.

> RESULT -> Didn't get the flag

![image](https://user-images.githubusercontent.com/70703371/227771307-2f79b68e-6b03-4421-855f-5ea3886b3735.png)


4. After reading the description again, maybe it uses a password to decode it, let's use `TCP1P` as the pass.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/227771374-d3e815fd-e841-4705-b73e-0bb8aa200b71.png)


5. Got the flag!


## FLAG

```
TCP1P{3Nc0D1ng_Typ3_Sp4m_w1Th_p4ssW0rd}
```
