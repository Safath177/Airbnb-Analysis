import pandas as pd
import streamlit as st
pd.set_option('display.max_columns',None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout='wide')
st.title(":bar_chart: AIRBNB DATA ANALYSIS")
st.write("")
tab1,tab2,tab3 = st.tabs([":house: Home",":question: About",":chart_with_upwards_trend: Data Exploration"])

def datafr():
    df = pd.read_csv("C:/Users/rsafatht/Documents/AirBNB/Airbnb.csv")
    return df

df = datafr()


with tab1:

    image_1 = Image.open("C:/Users/rsafatht/Documents/AirBNB/airbnb.jpeg")
    st.image(image_1)

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')
    
with tab2:


    st.header("ABOUT THIS PROJECT")

    st.subheader(":red[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')

    st.subheader(":red[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')

    st.subheader(":red[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')

    st.subheader(":red[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')

    st.subheader(":red[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')

with tab3:
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***","***GEOSPATIAL VISUALIZATION***","***TOP CHARTS***"])

    with tab1:
        st.title(":moneybag:**PRICE DIFFERENCE**")
        st.write("")
        st.write(''' Understand the factors that influence Airbnb pricing. Explore how location, room type, property type, and host response time impact the listing prices. Visualize the price differences across various attributes, such as the relationship between price, review scores, and number of reviews.
                    Use the interactive filters to find the perfect Airbnb stay that fits your budget and preferences. ''')

    
        col1,col2 = st.columns(2)

        with col1:

            country = st.selectbox("Select the Country",df["country"].unique())
            df1 = df[df["country"] == country]
            df1.reset_index(drop = True, inplace = True)

            room_ty = st.selectbox("Select the Room Type",df1["room_type"].unique())
            df2 = df1[df1["room_type"] == room_ty ]
            df2.reset_index(drop = True, inplace = True)

            df_bar = pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar, x = "property_type", y = "price", title= "Price based on Property",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Bluered_r,
                             width=500,height=500)
            st.plotly_chart(fig_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            property_ty = st.selectbox("Select the Property_type",df2["property_type"].unique())
            df4 = df2[df2["property_type"]== property_ty]
            df4.reset_index(drop = True, inplace = True)

            df_pie = pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace=True)

            fig_pie = px.pie(df_pie,values="price",names="host_response_time",hover_data=["bedrooms"],color_discrete_sequence=px.colors.sequential.Bluered_r,
                             title="Price Difference Based on Host Response Time",width=500,height=500)
            st.plotly_chart(fig_pie)

        col1,col2 = st.columns(2)

        with col1:

                hostresponsetime = st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

                df5 = df4[df4["host_response_time"] == hostresponsetime ]

                df_duration_bar = pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
                df_duration_bar.reset_index(inplace=True)

                fig_duration_bar = px.bar(df_duration_bar, x = "bed_type", y = ['minimum_nights','maximum_nights'],title='Pricing Based on Stay Duration',hover_data="price",
                                          barmode='group',color_discrete_sequence=px.colors.sequential.Bluered_r,width=500,height=500)
                st.plotly_chart(fig_duration_bar)

        with col2:

                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")

                df_acco_bar = pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
                df_acco_bar.reset_index(inplace=True)

                fig_acco_bar = px.bar(df_acco_bar, x= "bed_type", y = ["bedrooms","beds","accommodates"],hover_data="price",title="Pricing Based on Accomodation",
                                      barmode="group",color_discrete_sequence=px.colors.sequential.Bluered_r,width=500,height=500)
                
                st.plotly_chart(fig_acco_bar)

    with tab2:

        def datafr():
            df_avail = pd.read_csv("C:/Users/rsafatht/Documents/AirBNB/Airbnb.csv")
            return df_avail
        df_avail = datafr()

        st.title("**Availability Space**")
        st.write("")
        st.write('''Understand the occupancy patterns of Airbnb listings across different time frames.
                Explore the availability of spaces for 30 days, 60 days, 90 days, and even 365 days, broken down by room type, bed type, and location accuracy. Identify peak and off-peak seasons, and gain insights into how host response time affects the availability of listings.
                This analysis helps you find the optimal time to book your Airbnb stay.''')

        col1,col2 = st.columns(2)

        with col1:

            country_avail = st.selectbox("Country",df_avail["country"].unique())
            df1_avail = df[df["country"] == country_avail]
            df1_avail.reset_index(drop = True, inplace = True)

            property_ty_avail = st.selectbox("Property Type",df_avail["property_type"].unique())
            df2_avail = df[df["property_type"] == property_ty_avail]
            df2_avail.reset_index(drop = True, inplace = True)

            df_avail_sunbur_30 = px.sunburst(df2_avail,path=["room_type","bed_type","is_location_exact"],values="availability_30",width=600,height=500
                                          ,title="Availabilty of Spaces for 30 Days",color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(df_avail_sunbur_30)

        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_avail_sunbur_60 = px.sunburst(df2_avail,path=["room_type","bed_type","is_location_exact"],values="availability_60",width=600
                                             ,height=500,title="Availabilty of Spaces for 60 Days",color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(df_avail_sunbur_60)

        col1,col2 = st.columns(2)

        with col1:

                df_avail_sunbur_90 = px.sunburst(df2_avail,path=["room_type","bed_type","is_location_exact"],values="availability_90",width=600
                                             ,height=500,title="Availabilty of Spaces for 90 Days",color_discrete_sequence=px.colors.sequential.Bluered_r)
                st.plotly_chart(df_avail_sunbur_90)

        with col2:

            df_avail_sunbur_365 = px.sunburst(df2_avail,path=["room_type","bed_type","is_location_exact"],values="availability_365",width=600
                                            ,height=500,title="Availabilty of Spaces for 365 Days",color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(df_avail_sunbur_365)
        room_ty_avail = st.selectbox("Room Type",df2_avail["room_type"].unique())
        df3_avail = df2_avail[df2_avail["room_type"] == room_ty_avail]

        df_host_bar_avail = pd.DataFrame(df3_avail.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_host_bar_avail.reset_index(inplace=True)

        host_avail_bar = px.bar(df_host_bar_avail,x='host_response_time',y=["availability_30","availability_60","availability_90","availability_365"],
                                title="Availability based on Host response time",hover_data="price",barmode="group",color_discrete_sequence=px.colors.sequential.Bluered_r,width=1000)
        
        st.plotly_chart(host_avail_bar)

    with tab3:
        st.title("LOCATION ANALYSIS")
        st.write("")
        st.write(''' Dive into the price variations across different locations. Filter the listings by country, property type, and price range to uncover the factors that influence pricing.
                    Analyze the correlation between location-based attributes, such as accommodations and cleaning fees, to understand the drivers of Airbnb pricing in specific areas. ''')

        def datafr():
            df = pd.read_csv("C:/Users/rsafatht/Documents/AirBNB/Airbnb.csv")
            return df
        
        df_LA = datafr()

        country_LA = st.selectbox("Select the Country for Location Analysis",df_LA["country"].unique())

        df_LA_1 = df_LA[df_LA["country"] == country_LA]
        df_LA_1.reset_index(drop = True, inplace = True)

        property_LA = st.selectbox("Select the Property for Location Analysis", df_LA_1["property_type"].unique())

        df_LA_2 = df_LA_1[df_LA_1["property_type"]== property_LA]
        df_LA_2.reset_index(drop = True, inplace = True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df_LA_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_LA_2['price'].min())+' '+str("(30% of the value)"):
                df_val_30 = df_LA_2[df_LA_2['price'] <= differ_max_min*0.30+df_LA_2['price'].min()]
                df_val_30.reset_index(drop = True, inplace = True)
                return df_val_30
            
            elif sel_val == str(differ_max_min*0.30 + df_LA_2['price'].min()) +' '+str('to')+' '+str(differ_max_min*0.60 + df_LA_2['price'].min())+' '+str("(30% to 60% of the value)"):
                df_val_60 = df_LA_2[df_LA_2['price'] >= differ_max_min*0.30 + df_LA_2['price'].min()]
                df_val_60_1 = df_val_60[df_val_60['price'] <= differ_max_min*0.60 + df_LA_2['price'].min()]
                df_val_60_1.reset_index(drop = True, inplace = True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df_LA_2['price'].min()) +' '+str('to')+' '+str(df_LA_2['price'].max())+' '+str("(60% to 100% of the value)"):
                df_val_100 = df_LA_2[df_LA_2['price'] >= differ_max_min*0.60 + df_LA_2['price'].min()]
                df_val_100.reset_index(drop = True, inplace = True)
                return df_val_100
            
        
        differ_max_min = df_LA_2['price'].max() - df_LA_2['price'].min()

        val_sel = st.radio("Select the Price Range",[str(df_LA_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_LA_2['price'].min())+' '+str("(30% of the value)"),
                                                    str(differ_max_min*0.30 + df_LA_2['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_LA_2['price'].min())+' '+str("(30% to 60% of the value)"),
                                                    str(differ_max_min*0.60 + df_LA_2['price'].min())+' '+str('to')+' '+str(df_LA_2['price'].max())+' '+str("(60% to 100% of the Value)")])
        df_val_sel = select_the_df(val_sel)

        if df_val_sel is not None:
            df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                                "room_type", "bed_type","cancellation_policy",
                                                "images","host_url","host_name", "host_location",                   
                                                "host_response_time", "host_thumbnail_url",            
                                                "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                                "host_picture_url","host_neighbourhood",
                                                "host_identity_verified","host_verifications",
                                                "street", "suburb", "government_area", "market",                        
                                                "country", "country_code","location_type","is_location_exact",
                                                "amenities"]).corr()
            
            st.dataframe(df_val_sel_corr)

            df_val_sel_g = pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
            df_val_sel_g.reset_index(inplace=True)

            fig_LA_1 = px.bar(df_val_sel_g,x="accommodates",y=["cleaning_fee","bedrooms","beds"], title="Accommodates",
                                hover_data='extra_people',barmode='group',color_discrete_sequence=px.colors.sequential.Bluered_r,width=1000)
            st.plotly_chart(fig_LA_1)
            

    with tab4:

        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")
        st.write(''' Visualize the distribution of Airbnb listings on an interactive map. Explore the geographical spread of properties, with the size and color of the markers representing the number of accommodates and price, respectively.
                    Identify the hot spots and gain a spatial understanding of the Airbnb landscape. ''')
        
        fig_geo = px.scatter_mapbox(df,lat="latitude",lon="longitude",color="price",size="accommodates"
                                    ,color_continuous_scale="Rainbow",hover_name="name",range_color=(0,49000), mapbox_style="carto-positron",
                                    zoom=4)
        fig_geo.update_layout(width=1150,height=800,title="Geospatial Distribution of Listings")
        st.plotly_chart(fig_geo)

    with tab5:

        st.title("TOP 100!")
        st.write("")
        st.write(''' Discover the most desirable Airbnb listings based on price. Analyze the top 100 highest-priced properties, delving into details like stay duration, bedrooms, beds, and accommodations.
                    Understand the factors that contribute to the premium pricing of these exclusive Airbnb offerings.  ''')

        country_top_charts = st.selectbox("Select the Country for Top Charts",df["country"].unique())
        df_1_tc = df[df["country"] == country_top_charts]

        property_top_charts = st.selectbox("Select the Property for Top Charts",df["property_type"].unique())
        df_2_tc = df[df["property_type"]== property_top_charts]
        df_2_tc.reset_index(drop=True, inplace = True)

        df_2_sort = df_2_tc.sort_values(by="price")
        df_2_sort.reset_index(drop = True, inplace = True)

        df_price = pd.DataFrame(df_2_sort.groupby("host_neighbourhood")["price"].agg(['sum','mean']))
        df_price.reset_index(inplace=True)
        df_price.columns = ["host_neighbourhood","Total_Price", "Average_Price"]

        col1,col2 = st.columns(2)

        with col1:

            fig_price = px.bar(df_price,x="Total_Price",y="host_neighbourhood",orientation="h",title="Total Price Based on Host Neighbourhood"
                               ,width=600,height=800)
            st.plotly_chart(fig_price)
        
        with col2:

            fig_price_2 = px.bar(df_price,x="Average_Price",y="host_neighbourhood",orientation="h"
                                 ,title="Average Price Based on Host Neighbourhood",width=600,height=800)
            st.plotly_chart(fig_price_2)

        col1,col2 = st.columns(2)

        with col1:
            df_price_loc = pd.DataFrame(df_2_sort.groupby("host_location")["price"].agg(['sum','mean']))
            df_price_loc.reset_index(inplace=True)
            df_price_loc.columns = ["host_location","Total_Price","Average_Price"]

            fig_price_loc_tot = px.bar(df_price_loc,x="Total_Price",y="host_location",orientation='h',title="Total Price Based on Host Location"
                                   ,width=600,height=800,color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(fig_price_loc_tot)
        with col2:    
            fig_price_loc_avg = px.bar(df_price_loc,x="Average_Price",y="host_location",orientation="h",title="Average Price Based on Host Location",
                                       width=600,height=800,color_discrete_sequence=px.colors.sequential.Bluered_r)
            st.plotly_chart(fig_price_loc_avg)

        room_type_tc = st.selectbox("Select the Room Type for Top Charts",df["room_type"].unique())
        df_rt_tc = df_2_sort[df_2_sort["room_type"] == room_type_tc]
        df_3_sort = df_rt_tc.sort_values(by = "price")
        df_3_sort.reset_index(drop = True,inplace = True)
        df_top_50_prices = df_3_sort.head(100)

        fig_top_50_price_1= px.bar(df_top_50_prices, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df_top_50_prices["price"].max()),
                                title= "Stay Duration & Accommodations",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df_top_50_prices, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "rainbow",
                                 title= "Bedrooms, Beds, Accommodations & Bed type",
                                range_color=(0,df_top_50_prices["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])
        
        st.plotly_chart(fig_top_50_price_2)
