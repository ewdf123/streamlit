import streamlit as st


st.title('*기범고사*')
st.header('<응시전 확인사항>')
st.subheader('1번부터 15번까지는 객관식 문제이고 16번부터 20번까지는 주관식 문제입니다.')
st.caption('객관식은 각 문항당 4점이고 주관식은 각 문항당 8점입니다.')
a = 0
name = st.text_input(
    label='이름을 입력하세요?',
    placeholder='기믹범'
)

st.header('1번 문제')

image_path = '1694171831169.jpg'
st.image(image_path)

character = st.radio(
    '이 사진속 주인공의 이름은??',
    ('박도담', '기믹범', '금쪽이', '미르', '김기범'))
if character == '김기범':
    st.write('축하합니다!🎁 정답은 김기범입니다.')
    image_goat = 'IMG_20230909_093117_289.jpg'
    st.image(image_goat)
    a += 4
else:
    st.write('떙!')

st.header('2번 문제')

character = st.radio(
    '기범이의 나이는??',
    ('15살', '16살', '17살', '18살', '19살'))
if character == '16살':
    st.write('축하합니다!🎁 정답은 16살입니다.')
    a += 4
else:
    st.write('떙!')

st.header('3번 문제')

character = st.radio(
    '금쪽이의 생일은??',
    ('2월 29일', '4월 17일', '8월 6일', '10월 5일', '12월 26일'))
if character == '10월 5일':
    st.write('축하합니다!🎁 기범이의 생일은 10월 5일 입니다.')
    a += 4
else:
    st.write('떙!')
st.header('4번 문제')

character = st.radio(
    '기범이의 키는??',
    ('158.8(cm)', '169.3(cm)', '171.1(cm)', '173.7(cm)', '175.3(cm)'))
if character == '171.1(cm)':
    st.write('축하합니다!🎁 정답은 171.1(cm)입니다.')
    a += 4
else:
    st.write('떙!')

st.header('5번 문제')

character = st.radio(
    '기믹범의 몸무게는??',
    ('58(kg)', '60(kg)', '63(kg)', '65(kg)', '67(kg)'))
if character == '60(kg)':
    st.write('축하합니다!🎁 기범이는 60(kg)였습니다.')
    a += 4
else:
    st.write('떙!')

st.header('6번 문제')

character = st.radio(
    '기범이의 최애 애니는??',
    ('호리미야', '나의 행복한 결혼', '암살교실', '철야의 노래', '최애의 아이'))
if character == '최애의 아이':
    st.write('축하합니다!🎁 기범이의 최애 애니는 [최애의 아이]입니다.')
    a += 4
    image_ani = 'i.jpg'
    st.image(image_ani)
else:
    st.write('떙!')

st.header('7번 문제')

character = st.radio(
    '기범이가 가장 좋아하는 동물은??',
    ('도담', '강아지', '고양이', '쿼카', '카피바라'))
if character == '카피바라':
    st.write('축하합니다!🎁 기범이가 가장 좋아하는 동물은 카피바라입니다.')
    image_dodam = 'dodam.jpg'
    st.image(image_dodam)
    a += 4
else:
    st.write('떙!')

st.header('8번 문제')

character = st.radio(
    '김기범이 안 가본 나라는??',
    ('베트남', '일본', '태국', '필리핀', '중국'))
if character == '필리핀':
    st.write('축하합니다!🎁 기범이는 필리핀을 가보지 않았어요.')
    a += 4
else:
    st.write('떙!')

st.header('9번 문제')

character = st.radio(
    '기범이가 가고 싶은 나라는??',
    ('스위스', '미국', '이탈리아', '노르웨이', '인도'))
if character == '노르웨이':
    st.write('축하합니다!🎁 기범이는 노르웨이를 가고 싶다네요.')
    a += 4
else:
    st.write('떙!')

st.header('10번 문제')

character = st.radio(
    '기믹범이 가장 잘하는 챔피언은??',
    ('샤코', '탈론', '제드', '나피리', '카직스'))
if character == '탈론':
    st.write('축하합니다!🎁 기범이가 가장 잘하는 챔프는 탈론입니다.')
    image_lol = 'lol.jpg'
    st.image(image_lol)
    a += 4
else:
    st.write('떙!')

st.header('11번 문제')

character = st.radio(
    '김기범의 반려동물은??',
    ('도마뱀', '강아지', '고양이', '도마뱀', '고슴도치'))
if character == '강아지':
    st.write('축하합니다!🎁 기범이가 키우는 동물은 강아지였습니다.')
    image_dog = 'IMG_20230909_090103_576.jpg'
    st.image(image_dog)
    a += 4

else:
    st.write('떙!')

st.header('12번 문제')

character = st.radio(
    '기범이의 반려동물의 이름은??',
    ('도담이', '미르', '머랭이', '달래', '기믹범'))
if character == '미르':
    st.write('축하합니다!🎁 기범이의 강아지 이름은 [미르]였습니다.')
    a += 4
else:
    st.write('떙!')

st.header('13번 문제')

character = st.radio(
    '기믹범의 반려 동물의 나이는??',
    ('1살', '3살', '5살', '7살', '9살'))
if character == '9살':
    st.write('축하합니다!🎁 기범이의 반려동물은 9살입니다.')
    a += 4
else:
    st.write('떙!')

st.header('14번 문제')

character = st.radio(
    '김기범의 안티팬은??',
    ('박옥준', '이도담', '최주원', '진우협', '김민재'))
if character == '최주원':
    st.write('축하합니다!🎁 기범이의 안티팬은 [최주원]입니다.')
    a += 4
else:
    st.write('떙!')

st.header('15번 문제')

character = st.radio(
    '기범이의 현재 통장 잔고는??',
    ('3,420원', '11,786원', '56,620원', '93,472원', '154,320원'))
if character == '11,786원':
    st.write('축하합니다!🎁 기범이의 현재 통장 잔고는 11,786원입니다')
    a += 4
else:
    st.write('떙!')

st.header('16번 문제')

insta = st.text_input(
    label='김기범의 인스타는??',
    placeholder='mcdreamy._.b'
)
if insta == 'mcdreamy._.b':
    st.write("정답입니다.")
    image_insta = 'Screenshot_20230909_090518_Instagram.jpg'
    st.image(image_insta)
    a += 8
else:
    st.write('다시 정답을 입력하세요.')

st.header('17번 문제')

wjs = st.text_input(
    label='기믹범의 전여친 수는??',
    placeholder='0(명)'
)
if wjs == '2':
    st.write("정답입니다.")
    a += 8
elif wjs == '2명':
    st.write('정답입니다.')
    a += 8
else:
    st.write('다시 정답을 입력하세요.')

st.header('18번 문제')

i22 = st.text_input(
    label='기범이의 여자친구는??',
    placeholder='호리 쿄코'
)
if i22 == '아카네':
    st.write("정답입니다.")
    image_acne = 'i22.jpeg'
    st.image(image_acne)
    a += 8
else:
    st.write('다시 정답을 입력하세요.')

st.header('19번 문제')

song = st.text_input(
    label='기범이가 가장 좋아하는 노래는??',
    placeholder='라일락'
)
if song == '사임쌓임':
    st.write("정답입니다.")
    image_song = 'Screenshot_20230909_092540_Melon.jpg'
    st.image(image_song)
    a += 8
else:
    st.write('다시 정답을 입력하세요.')

st.header('20번 문제')

count = st.text_input(
    label='이때까지 나온 [기믹범]의 개수는???',
    placeholder='13개'
)
if count == '8':
    st.write("정답입니다.")
    a += 8
elif count == '8개':
    st.write('정답입니다.')
    a += 8
else:
    st.write('다시 정답을 입력하세요.')

st.header('수고하셨습니다.')
st.header(f':blue[{name}] 님의 점수: :red[{a}]')
st.subheader('0~20점 : 기범이가 누구야?')
st.subheader('20~40점 : 김기범 아 걔?ㅋ')
st.subheader('40~60점 : 기믹범을 모른다고??')
st.subheader('60~80점 : 기범아 거리 좀 둘까?')
st.subheader('0~20점 : 김기범이 누구야??')

if a <= 20:
    image_bum = 'rlarlqja22.jpg'
    st.image(image_bum)

elif a <= 40:
    image_bum = '1694171836777.jpg'
    st.image(image_bum)

elif a <= 60:
    image_bum = 'IMG_20230909_101820_040.jpg'
    st.image(image_bum)

elif a <= 80:
    image_bum = '1694171833600.jpg'
    st.image(image_bum)

else:
    image_bum = 'IMG_20230909_090059_444.jpg'
    st.image(image_bum)
st.caption(':red[*이 페이지의 저작권은 김기범에게 있으며 불법복제 및 공유는 법적책임을 피할 수 있습니다.]')
