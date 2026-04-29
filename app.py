import streamlit as st
import pandas as pd

# ----- Background & Styling -----
st.markdown(
    """
    <style>
    /* Overall app background */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1525351484163-7529414344d8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Overlay for main content */
    .css-18e3th9 {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
    }

    /* Table styling */
    .stTable table {
        background-color: #FFA500;  /* orange background for menu table */
        color: #000000;  /* black text for clarity */
        font-weight: bold;
    }

    /* Table header styling */
    .stTable thead th {
        background-color: #FF8C00;  /* darker orange for headers */
        color: #FFFFFF;
        font-size: 18px;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #FFD700;  /* gold headers */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- Expanded Menu -----
menu = {
    'Tea': 10, 'Coffee': 20, 'Pasta': 60, 'Burger': 70, 'Pizza': 80,
    'Sandwich': 80, 'Dosa': 100, 'Idli': 30, 'Vada': 25, 'Samosa': 15,
    'Paneer Butter Masala': 120, 'Chole Bhature': 90, 'Fried Rice': 70,
    'Noodles': 60, 'Ice Cream': 50, 'Cold Drink': 25, 'Momos': 40, 'French Fries': 35
}

# Create DataFrame with serial numbers
menu_df = pd.DataFrame(list(menu.items()), columns=["Item", "Price (₹)"])
menu_df.reset_index(drop=True, inplace=True)  # remove old index
menu_df.index += 1  # start serial numbers from 1
menu_df.index.name = 'S.No'  # name the index column

# ----- Tabs -----
tab1, tab2, tab3, tab4 = st.tabs(["Menu", "Order", "Billing", "Reports"])

# ----- MENU TAB -----
with tab1:
    st.markdown("## 🍽️ Welcome to Pratham Restaurant")  # <-- Added headline
    st.header("☕ Cafe Menu")
    st.table(menu_df)  # nicely formatted with S.No, Item, Price


# ----- ORDER TAB -----
with tab2:
    st.header("🛒 Place Your Order")
    for item, price in menu.items():
        qty = st.number_input(f"{item} (₹{price})", min_value=0, step=1, key=item)
        if qty > 0:
            if "orders" not in st.session_state:
                st.session_state.orders = {}
            st.session_state.orders[item] = qty
        elif "orders" in st.session_state and item in st.session_state.orders:
            del st.session_state.orders[item]

    if st.button("Add/Update Order"):
        if "orders" in st.session_state and st.session_state.orders:
            st.success("Order added/updated!")
            st.json(st.session_state.orders)
        else:
            st.warning("No items selected.")

# ----- BILLING TAB -----
with tab3:
    st.header("💰 Billing")
    if "orders" in st.session_state and st.session_state.orders:
        bill_df = pd.DataFrame(
            [(item, qty, menu[item]*qty) for item, qty in st.session_state.orders.items()],
            columns=["Item", "Quantity", "Price (₹)"]
        )
        total = bill_df["Price (₹)"].sum()
        st.table(bill_df)
        st.markdown(f"### Total: ₹{total}")

        # Add to total sales
        if "total_sales" not in st.session_state:
            st.session_state.total_sales = {}
        for item, qty in st.session_state.orders.items():
            if item in st.session_state.total_sales:
                st.session_state.total_sales[item] += qty
            else:
                st.session_state.total_sales[item] = qty

        if st.button("Clear Order"):
            st.session_state.orders = {}
            st.success("Order cleared.")
    else:
        st.info("No orders yet. Please go to the Order tab first.")

# ----- REPORTS TAB -----
with tab4:
    st.header("📊 Sales Report")
    if "total_sales" in st.session_state and st.session_state.total_sales:
        report_df = pd.DataFrame(
            list(st.session_state.total_sales.items()),
            columns=["Item", "Total Sold"]
        )
        st.table(report_df)
        st.bar_chart(report_df.set_index("Item"))
    else:
        st.info("No sales yet. Place some orders first.")

        print("Test update")

st.write("Test update")