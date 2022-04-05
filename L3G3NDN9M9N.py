import mechanize
import facebook
import time

# Browser
br = mechanize.Browser()



# Browser settings
br.set_handle_equiv( True )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )


br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
br.open("https://www.facebook.com/")
br.geturl()

print ("[+] TH3 N9M9N [+]")
print ("[+] by N9M9N P4ndiiT [+]")
msg=str(input("Enter your Token : "))
poct=str(input("Enter your post Link : "))


token=msg
def auto_post():
 
 while True:
    graph = facebook.GraphAPI(access_token=token,version='2.8')
    
    graph.put_object(parent_object= poct, connection_name='comments',message='N9M9N H3R3')
    print ("han chla gya comment!\n")
    time.sleep(15)
    
    graph.put_object(parent_object=poct, connection_name='comments',message='<3 (_=_) :D (o/-/(-_-) :D (o \\(^^^) <(") \\-_-)(o <3 (_=_) <3 (o/-/(-_-) :D (o \\!!](_=_) <(") [[^]]\\-_-)(o♥ #4RY9N_KII_SIIS_F33L_MY (_|_) =D (_=_) (^^^) (o/-/(-_-) :D (o \\_=_) <(") \\-_-)(o <3 (_=_) <3 (o/-/[^](-_-) :D ([^]o \\_=_) <(") \\-_-)(o♥ (_=_) [!!^ <3 ([^]/-/(-_-) :D(o <3
[[___---#ITS_M0ST__W9NT3D__L3G3ND_N0N__ST0P__F9D3B99Z__N0M4N__0WN__F11R3__4KK4__KH0F 3:) :v :D ||> =]] :) (^^^) :P (Y) ||> =P <3 ]]')
    print ("han chla gya comment!\n")
    time.sleep(20)
    graph.put_object(parent_object=poct, connection_name='comments',message='#9RY9N__K1__R9MD1__D1D1__K0__P2K__P2K__K9R__X0MD93__W9L9___$: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $: $:
#_____________NOM9N________H3R3(Y))
    print ("han chla gya comment!\n")
    time.sleep(10)
    graph.put_object(parent_object=poct, connection_name='comments',message=' <3 [[ 8| [-Y2R) _ <3 _ R-]] 3:) ]] 3:) (^^^) <3 T H 3;____) (^^^) =D =D [[ K H 0 F ]] (^^^) 8| <3 [[ M 4 K 3 R ]] <3 8| (^^^) ]] 8| <3 8| <(") (Y) <3 ______)) [[ #_____MR____N0M4N_____H3R3______ 3:) (Y) 8| ]]')
    print ("han chla gya comment!\n")
    time.sleep(10)

    
if __name__ == '__main__':
    auto_post()
    print ("han chla gya comment!\n")
#Code agar copy krte ho to nam mt htana made by N9M9N P9NDIT

