import os
import sys

system = sys.platform


def BanerAdm():
	""" Baner script """

	if system == "win32":
		os.system("cls")
		print("""\033[36m                                                                       
       \`*-.                    
        )  _`-.                 
        .  : `. .                 \033[31m[*]\033[m\033[1m Scaner Admin Pages in websites\033[m
\033[36m        : _   '  \                \033[31m[*]\033[m\033[1m Coded by: \033[m\033[1;36mNano\033[m
\033[36m        ; *` _.   `*-._           \033[31m[*]\033[m\033[1m Telegram: https://t.me/rdzin9\033[m
\033[36m        `-.-'          `-.        \033[31m[*]\033[m\033[1m Save in: \033[m\033[1;33mFound.txt \033[m
\033[36m          ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
\033[36m         :  '  |    ;       ;-.  \033[1m ➤ Tipos de URL: \033[m\033[1;33mhttps://example.com/ ou http://example.com/ \033[m
\033[36m         ; '   : :`-:     _.`* ;                   \033[m\033[1;4m ➤ www. é opcional! \033[m
\033[36m     .*' /  .*' ; .*`- +'  `*'  
      `*-*   `*-*  `*-*'                               \033[m\n""")
	elif system == "linux":
		os.system("clear")
		print("""\033[36m                                                                       
       \`*-.                    
        )  _`-.                 
        .  : `. .                 \033[31m[*]\033[m\033[1m Scaner Admin Pages in websites\033[m
\033[36m        : _   '  \                \033[31m[*]\033[m\033[1m Coded by: \033[m\033[1;36mNano\033[m
\033[36m        ; *` _.   `*-._           \033[31m[*]\033[m\033[1m Telegram: https://t.me/rdzin9\033[m
\033[36m        `-.-'          `-.        \033[31m[*]\033[m\033[1m Save in: \033[m\033[1;33mFound.txt \033[m
\033[36m          ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
\033[36m         :  '  |    ;       ;-.  \033[1m ➤ Tipos de URL: \033[m\033[1;33mhttps://example.com/ ou http://example.com/ \033[m
\033[36m         ; '   : :`-:     _.`* ;                   \033[m\033[1;4m ➤ www. é opcional! \033[m
\033[36m     .*' /  .*' ; .*`- +'  `*'  
      `*-*   `*-*  `*-*'                               \033[m\n""")
#.
