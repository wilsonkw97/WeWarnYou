<h1 align="center">WeWarnYou</h1>
<h4>The flood crisis which has started in Dec 17, 2021, has since hit 8 states in Malaysia. In certain areas, residents are hit with landslides. Having claimed 50 peoples' lives across 3 different states and displacing 125,490 citizens from their homes, this flood incident has last happened back in 1971 according to our King. The idea behind this project is to create a support system amongst the people in the country to help alert one another when another similar crisis occurs, rather than waiting for alerts by the NADMA which may come late.</h4>

"Source 1 : https://reliefweb.int/report/malaysia/malaysia-floods-and-landslides-update-nadma-met-malaysia-media-echo-daily-flash-3" 

"Source 2 : https://floodlist.com/asia/malaysia-floods-january-2022" 

<!-- Table of Contents -->
# Table of Contents
<li>
    <a href ="#Data Source">Data Source</a>
</li>
<li>
    <a href="#Website Building">Website Building</a>
</li>
<li>
    <a href="#About WeWarnYou">About WeWarnYou</a>
</li>
<li>
    <a href="#System Requirements">System Requirements</a>
</li>

<!-- Table of Contents -->

<!-- Data Source -->
## Data Source
* The data is scraped from Twitter based on the following keywords:
    + #daruratbanjir
    + #banjir2021
    + banjir Malaysia
    + flood Malaysia

* Stored in CSV format with 7461 rows for three weeks ranging from 25 December 2021 up to 14 January 2022.
<!-- Data Source -->

<!-- Website Building -->
## Website Building
We adopt the Django website framework to build up our web application, and use the <a href = "https://appseed.us/admin-dashboards/django-dashboard-volt">Django Volt Dashboard</a> as part of our dashboard template
<!-- Website Building -->

<!-- About WeWarnYou -->
## About WeWarnYou
Upon logging in with your registered credentials, you will be redirected to this page as below.
![Home Landing Page](https://github.com/wilsonkw97/WeWarnYou/blob/main/Home%20Landing%20Page.png?raw=true)
<!-- About WeWarnYou -->

<!-- System Requirements -->
## System Requirements
* The requirements for this application is stored in the requirements.txt for you to install into your OS.
    ```sh
    pip install -r requirements.txt
    ```
<!-- System Requirements -->