import streamlit as st
import pandas as pd
import requests
import math
# Page config must be first
st.set_page_config(page_title="Consumer Complaint Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("../data/rows.csv")  # Adjust path if needed

# Sidebar filters
st.sidebar.title("🔍 Filter Complaints")

states = sorted(df["State"].dropna().unique())
selected_state = st.sidebar.selectbox("📍 Select State", states)

companies_in_state = df[df["State"] == selected_state]["Company"].dropna().unique()
selected_company = st.sidebar.selectbox("🏦 Select Company", sorted(companies_in_state))

filtered_df = df[(df["State"] == selected_state) & (df["Company"] == selected_company)]

# Tabs for main sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard", "🔍 Explorer", "🧠 NLP Query", "🆔 Complaint Lookup", "🏦 Company Profile"
])

# Tab 1: Dashboard Overview
with tab1:
    st.header("📊 Complaint Dashboard Overview")
    st.metric("Total Complaints", len(df))
    st.metric("Complaints in Selected State", len(df[df["State"] == selected_state]))
    st.metric("Complaints for Selected Company", len(filtered_df))

    st.subheader("📈 Top Issues")
    st.bar_chart(filtered_df["Issue"].value_counts())

    st.subheader("📅 Complaints Over Time")
    st.line_chart(filtered_df["Date received"].value_counts().sort_index())

# Tab 2: Complaint Explorer
with tab2:
    st.header(f"🔍 Complaints for {selected_company} in {selected_state}")
    if filtered_df.empty:
        st.warning("⚠️ No complaints found.")
    else:
        selected_id = st.selectbox("🆔 Select Complaint ID", filtered_df["Complaint ID"].unique())
        complaint = filtered_df[filtered_df["Complaint ID"] == selected_id].iloc[0]

        st.write(f"**Product:** {complaint['Product']}")
        st.write(f"**Issue:** {complaint['Issue']}")
        st.write(f"**Company response:** {complaint['Company response to consumer']}")
        st.write(f"**Disputed?** {complaint['Consumer disputed?']}")

        with st.expander("📜 Full Narrative"):
            st.markdown(f"> {complaint['Consumer complaint narrative']}")

        with st.spinner("Generating summary..."):
            response = requests.post("http://127.0.0.1:8000/summarize", json={"query": complaint['Consumer complaint narrative']})
            if response.status_code == 200:
                st.success("📝 Summary:")
                st.markdown(f"> {response.json()['summary']}")

# Tab 3: NLP Query Summarizer
with tab3:
    st.header("🧠 NLP Query Summarizer")
    query = st.text_input("Enter your query", placeholder="e.g. credit report errors in Texas")
    if st.button("Summarize"):
        with st.spinner("Generating summary..."):
            response = requests.post("http://127.0.0.1:8000/summarize", json={"query": query})
            if response.status_code == 200:
                st.success("✅ Summary:")
                st.write(response.json()["summary"])
            else:
                st.error("❌ Failed to get summary.")

# Tab 4: Complaint ID Lookup
# Tab 4: Complaint ID Lookup
with tab4:
    st.header("🆔 Complaint ID Lookup")

    complaint_id_input = st.text_input("Enter Complaint ID", placeholder="e.g. 3189109")

    if st.button("Lookup Complaint") and complaint_id_input:
        try:
            cid = int(complaint_id_input)

            # Call FastAPI to get complaint details
            response = requests.get(f"http://127.0.0.1:8000/complaint/{cid}")
            data = response.json()

            if response.status_code == 200 and "error" not in data:
                st.success("✅ Complaint Found")

                # Display metadata
                st.write(f"**Date received:** {data.get('Date received', '—')}")
                st.write(f"**Product:** {data.get('Product', '—')}")
                st.write(f"**Issue:** {data.get('Issue', '—')}")
                st.write(f"**Company:** {data.get('Company', '—')}")
                st.write(f"**Submitted via:** {data.get('Submitted via', '—')}")
                st.write(f"**Company response:** {data.get('Company response to consumer', '—')}")
                st.write(f"**Timely response?** {data.get('Timely response?', '—')}")
                st.write(f"**Consumer disputed?** {data.get('Consumer disputed?', '—')}")

                # Show narrative
                st.subheader("📜 Complaint Narrative")
                raw_text = data.get("Narrative", "")
                if isinstance(raw_text, float) and (math.isnan(raw_text) or math.isinf(raw_text)):
                    raw_text = ""

                if not str(raw_text).strip():
                    st.warning("⚠️ No valid complaint narrative found for summarization.")
                else:
                    st.markdown(f"> {raw_text}")

                    # Generate summary
                    with st.spinner("Generating summary..."):
                        summary_response = requests.post(
                            "http://127.0.0.1:8000/summarize",
                            json={"query": str(raw_text)}
                        )
                        if summary_response.status_code == 200:
                            st.success("📝 Summary:")
                            st.markdown(f"> {summary_response.json()['summary']}")
                        else:
                            st.error("❌ Failed to get summary.")
            else:
                st.error("❌ Complaint not found.")
        except ValueError:
            st.error("⚠️ Invalid ID format. Please enter a numeric Complaint ID.")


# Tab 5: Company Profile
with tab5:
    st.header(f"🏦 Company Profile: {selected_company}")
    company_df = df[df["Company"] == selected_company]

    st.write(f"**Total complaints:** {len(company_df)}")
    st.write(f"**Top issues:**")
    st.bar_chart(company_df["Issue"].value_counts())

    st.write(f"**Dispute rate:**")
    st.write(company_df["Consumer disputed?"].value_counts(normalize=True))

    st.write(f"**Timely response rate:**")
    st.write(company_df["Timely response?"].value_counts(normalize=True))
# import streamlit as st
# import requests
# import pandas as pd
# st.set_page_config(page_title="Complaint Summarizer", layout="centered")

# df = pd.read_csv("cleaned_complaints.csv")

# st.sidebar.title("🔍 Filter Complaints")

# # Step 1: Select State
# states = sorted(df["State"].dropna().unique())
# selected_state = st.sidebar.selectbox("📍 Select State", states)

# # Step 2: Filter Companies in that State
# companies_in_state = df[df["State"] == selected_state]["Company"].dropna().unique()
# selected_company = st.sidebar.selectbox("🏦 Select Company", sorted(companies_in_state))

# filtered_df = df[(df["State"] == selected_state) & (df["Company"] == selected_company)]

# st.write(f"📊 Showing {len(filtered_df)} complaints for **{selected_company}** in **{selected_state}**")

# st.dataframe(filtered_df[[
#     "Complaint ID", "Date received", "Product", "Issue", "Company response to consumer"
# ]])


# # 🔽 Paste this below your imports
# def display_complaint(data, cid):
#     st.subheader(f"📄 Complaint ID: {cid}")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write(f"**Date received:** {data['Date received']}")
#         st.write(f"**Product:** {data['Product']}")
#         st.write(f"**Sub-product:** {data.get('Sub-product', '—')}")
#         st.write(f"**Issue:** {data['Issue']}")
#         st.write(f"**Sub-issue:** {data.get('Sub-issue', '—')}")

#     with col2:
#         st.write(f"**Company:** {data['Company']}")
#         st.write(f"**State:** {data['State']}")
#         st.write(f"**ZIP code:** {data.get('ZIP code', '—')}")
#         st.write(f"**Submitted via:** {data['Submitted via']}")
#         st.write(f"**Tags:** {data.get('Tags', '—')}")

#     st.write(f"**Company response to consumer:** {data['Company response to consumer']}")
#     st.write(f"**Timely response?** {data['Timely response?']}")
#     st.write(f"**Consumer disputed?** {data['Consumer disputed?']}")

#     with st.expander("📜 Full Complaint Narrative"):
#         st.markdown(f"> {data['Narrative']}")

#     with st.spinner("Generating summary..."):
#         summary_response = requests.post(
#             "http://127.0.0.1:8000/summarize",
#             json={"query": data["Narrative"]}
#         )
#         if summary_response.status_code == 200:
#             st.success("📝 Summary:")
#             st.markdown(f"> {summary_response.json()['summary']}")

# st.title("📋 Consumer Complaint Summarizer")
# st.write("Enter a query to retrieve and summarize complaints using your RAG pipeline.")

# query = st.text_input("🔍 Enter your query", placeholder="e.g. credit report errors")

# if st.button("Summarize") and query:
#     with st.spinner("Generating summary..."):
#         response = requests.post("http://127.0.0.1:8000/summarize", json={"query": query})
#         if response.status_code == 200:
#             summary = response.json()["summary"]
#             st.success("✅ Summary:")
#             st.write(summary)
#         else:
#             st.error("❌ Failed to get summary. Check FastAPI server.")
# st.subheader("🔍 Search by Complaint ID")

# complaint_id_input = st.text_input("Enter Complaint ID", placeholder="e.g. 3189109")

# if st.button("Lookup Complaint") and complaint_id_input:
#     try:
#         cid = int(complaint_id_input)
#         response = requests.get(f"http://127.0.0.1:8000/complaint/{cid}")
#         data = response.json()

#         if response.status_code == 200 and "error" not in data:
#             st.success("✅ Complaint Found:")
#             st.write(f"**Date received:** {data['Date received']}")
#             st.write(f"**Product:** {data['Product']}")
#             st.write(f"**Issue:** {data['Issue']}")
#             st.write(f"**Company:** {data['Company']}")
#             st.write("**Narrative:**")
#             st.markdown(f"> {data['Narrative']}")

#             # 🔁 Add summarization here
#             if "Narrative" in data:
#                 summary_response = requests.post(
#                     "http://127.0.0.1:8000/summarize",
#                     json={"query": data["Narrative"]}
#                 )
#                 if summary_response.status_code == 200:
#                     st.write("**📝 Summary:**")
#                     st.markdown(f"> {summary_response.json()['summary']}")
#                 else:
#                     st.warning("⚠️ Failed to summarize complaint.")
#         else:
#             st.error("❌ Complaint not found.")
#     except ValueError:
#         st.error("⚠️ Please enter a valid numeric Complaint ID.")
