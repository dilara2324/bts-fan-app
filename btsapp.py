bts_info = """
BTS - Janubiy Koreyaning mashhur K-pop guruhu
A'zolari: Rm, Jin, Suga, J-hope, Jimin, V, Jungkook
Debyut: 2013-yil
Kompaniya: HYBE (BigHit Entertainment)
Fanlar nomi: ARMY
"""
st.title("🎤 BTS FAN APP")

# Foydalanuvchi login (oddiy input)
username = st.text_input("Login kiriting:")
password = st.text_input("Parol kiriting:", type="password")

if username and password:
    st.write(f"\nXush kelibsiz, {username}!")
    st.write("---BTS HAQIDA MA'LUMOT---")
    st.write(bts_info)

# Savollar
questions = [
  ("BTS nechanchi yilda debyut qilgan?", "2013")
  ("BTS fanlari nima deb nima deb ataladi?", "ARMY"),
  ("BTS nechta a'zodan iborat?", "7")
  ("BTS kompaniyasi nomi?", "HYBE")
  ("BTS guruhining lideri kim?", "RM")
]
if "score" not in st.session_state:
  st.session_state.score = 0
  st.session_state.q_index = 0

if st.session_state.q_index < len(questions):
  q, correct = questions[st.session_state.q_index]

st.write(f"**Savol {st.session_state.q_index + 1}:** {q}"]
answer = st.text_input("Javobingiz:", key=st.session_state.q_index)

if st.button("Tekshirish"):
  if answer.lower() == correct:
    st.succes("To'g'ri!)
    st.st.session_state.score += 1
else:
  st.error("Noto'g'ri")

st.session_state.q_index += 1
st.rerun()

else:
    st.succes(f"Test tugadi! Siz {st.session_state.score} ta armypoint oldingiz")


