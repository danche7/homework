import streamlit as st

def start_button():
        if st.session_state.name:
            st.session_state.page = "quiz"
            st.session_state.index=0      


def state1():
    st.title("How much do you know about me???")
    st.text_input("Your name", key="name")
    if st.session_state.name:
        st.write("Hello there", st.session_state.name)
    st.button("Start", on_click=start_button)


def nextb():
    st.session_state.index+=1

def endb():
    st.session_state.page="done"

def quiz_state(questions):
    ind = st.session_state.index
    t = len(questions)

    question, answer = questions[ind]
    st.write(question)


    if ind == 3:
        user_a = st.selectbox("Pick one", ["", "milk","chocolate milk","orange juice"])
    else:
        user_a = st.text_input("Answer the question", key=f"answeri{ind}")

    if user_a:
        if user_a.lower().strip() == answer.lower().strip():
            st.success("Correct!")

        else:
            st.error("Wrong!")
            st.write(f"Correct answer: {answer}")

        if ind+1 < t:
            st.button("Next", on_click=nextb)
        else:
            st.button("End", on_click=endb)




def end_page():
    st.success("You've completed the quiz!")
    st.button("Restart", on_click=restart)

def restart():
    st.session_state.page = "welcome"
    st.session_state.name = ""
    st.session_state.index = 0
    st.session_state.answer = ""


def main():
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    if "name" not in st.session_state:
        st.session_state.name = ""

    questions = [
        ["What is my favourite color?", "purple"],
        ["What type of pet do I have?", "dog"],
        ["What is my least favourite subject?", "physics"],
        ["What is my favourite sweet drink?", "chocolate milk"],
    ]

    if st.session_state.page == "welcome":
        state1()
    elif st.session_state.page == "quiz":
        quiz_state(questions)
    elif st.session_state.page == "done":
        end_page()

main()
