import streamlit as st

st.title("Title->GFG")
st.header("Header->GfG")
st.subheader("Subheader->GfG")
st.text("Text->GfG")

st.markdown('#Hi')
st.markdown('##Hi')
st.markdown('###Hi')

st.success("Success")
st.info('Information')
st.warning('Warning')
st.error('Error')
st.exception(ZeroDivisionError('Division not possible'))

st.write(range(1,10))
st.write(1+2+3)

st.code('x=10\nfor i in range(x):\n\tprint(i)')


if(st.checkbox('Adult')):
    st.write('you are an adult!')

#radioButton
radioButton=st.radio('Select:',('Male','Female','Other'))
if(radioButton=='Male'):
    st.write("You're a male")
elif(radioButton=='Female'):
    st.write("You're a Female")
elif(radioButton=='Other'):
    st.write("You're an other")

#dropdown
st.subheader('Select Box')
SelectBox=st.selectbox('Data:',['DA','ML','AI','NLP','CV'])
st.write('You have selected:', SelectBox)

#Button
st.subheader('Button')
if(st.button('Click me')):
    st.write('THanks for clicking me')

#Slider
st.subheader('Slider')
vol=st.slider('Select the volume',0,100,step=1)
st.write('Volume is:',vol)

#Text_input
st.subheader('Text_input')
username=st.text_input('username')
password=st.text_input('password',type='password')

#Age
st.subheader('Age')
st.number_input('Select your age',18,20)

#Date
st.subheader('Date')
st.date_input('Date')

#Time
st.subheader('Time')
st.time_input('Time')
