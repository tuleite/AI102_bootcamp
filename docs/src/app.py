import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card
def configure_interface():
    st.title("Files Upload - AI102 Bootcamp Challenge")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        file_name = uploaded_file.name
        #send to the blob storage
        blob_url = upload_blob(uploaded_file, file_name)
        if blob_url:
            st.write(f"File {file_name} was send successfully to Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url)
            show_image_validation(blob_url, credit_card_info)
        else:
            st.write(f"Error while sending {file_name} to Azure Blob Storage")


def show_image_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Sent image", use_column_width=True)
    st.write("Validation results:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Valid Credit Card</h1>", unsafe_allow_html=True)
        st.write(f"Client's name: {credit_card_info["card_name"]}")
        st.write(f"Bank name: {credit_card_info['bank_name']}")
        st.write(f'Expiration date: {credit_card_info['expiry_date']}')
    else:
        st.markdown(f"<h1 style='color: red;'>Invalid Credit Card</h1>")
        st.write("This is not a valid Credit Card.")


if __name__ == "__main__":
    configure_interface()