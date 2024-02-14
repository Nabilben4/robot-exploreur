import streamlit as st
import paho.mqtt.client as mqtt

mqtt_broker = "pimqtt.local"
mqtt_port = 1883


mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)

    
def send_message(value,mqtt_topic):
    message = str(value)
    mqtt_client.publish(mqtt_topic, message)

st.title("TEST moteur robot explorateur")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.subheader("COUDE AXE 3")
    if st.button('HAUt'):
       send_message(0,"test/pwm1")  

    if st.button('BAs'):
       send_message(2047,"test/pwm1") 

    if st.button('0'):
       send_message(1023,"test/pwm1") 

with col3:
    st.subheader("PINCE AXE 5")
    
    if st.button('FERME'):
       send_message(0,"test/pwm2")  

    if st.button('OUVERT'):
       send_message(2047,"test/pwm2") 

    if st.button('00'):
       send_message(1023,"test/pwm2") 
with col2:
    st.subheader("BRAS AXE 2")
    if st.button('HAUT'):
       send_message(0,"test/pwm3")  

    if st.button('BAS'):
       send_message(2047,"test/pwm3") 

    if st.button('000'):
       send_message(1023,"test/pwm3") 
with col4:
    st.subheader("rotation pince AXE 4 ")
    if st.button('anti HORAIRE'):
       send_message(0,"test/pwm4")  

    if st.button('HORAIRE'):
       send_message(2047,"test/pwm4") 

    if st.button('0000'):
       send_message(1023,"test/pwm4") 


#st.subheader("PINCE AXE 5")
#moteur2 = st.slider("commande moteur 2",0,2047,1024)
#send_message(moteur2,"test/pwm2")

#st.subheader("rotation pince AXE 4")
#moteur3 = st.slider("commande moteur 3",0,2047,1024)
#send_message(moteur3,"test/pwm3")


#st.subheader("BRAS AXE 2")
#moteur4 = st.slider("commande moteur 4",0,2047,1024)
#send_message(moteur4,"test/pwm4")




    
mqtt_client.loop()

if st.button('STOP'):
    send_message(1024,"test/pwm1")
    send_message(1024,"test/pwm2")
    send_message(1024,"test/pwm3")
    send_message(1024,"test/pwm4")
    

