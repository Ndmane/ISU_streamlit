import requests
import streamlit as st
from streamlit_lottie import st_lottie

class Home:
    def __init__(self):
        pass

    def app(self):

        def load_lottieurl(url):
            r = requests.get(url)
            if r.status != 200:
                return None
            return r.json()

        with st.container():
            st.subheader("Hello there")
            st.title("I'm Dias Akhmadiyev and this is hoe page for my streamlit project")
            st.write("In short, about me: a third-year student at NKU, a nerd in computer games, I like to draw, listen to audiobooks and music.")
            st.write("[My insta >](https://www.instagram.com/bez5566/profilecard/?igsh=Z2lxcXV6OGVzMXJ6)")
            st.write("[Telegram channel >](https://t.me/+MpWflxzRhcoyNTdi)")

        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("Why am I like this?")
                st.write(
                """
                I first got to know the world of computer games at the age of five. Then Dad brought home some kind of box that I didn't understand.
                A few hours later, he returned and connected her to the TV. I was immediately surprised because something unusual had started,
                because before that we had only watched TV shows on TV. After some time, I was allowed to play myself, so the first game in my life turned out to be Tekken 5.
                Then I just thought it was an ordinary fight, but soon more and more disks were restored, we had the Internet and somehow everything started spinning.
                I got my first computer at the age of 16, even then I knew what steam, AAA games and other terms that a normal person would never need in their life.
                Since 2020, I have been actively playing basically everything, and so we are getting closer to today, now I am typing this text.
                I hope that life will only get better from now on.
                """
                )

                st.write("[My steam profile >](https://steamcommunity.com/id/nochnoieblan/)")
