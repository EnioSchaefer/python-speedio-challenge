import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimilarWebScraping:
    def __init__(self, url: str) -> None:
        self.__url = url

    async def scrape_data(self):
        chrome_options = Options()

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"' ,
            'x-requested-with': 'XMLHttpRequest',
            'x-sw-page': 'https://pro.similarweb.com/',
            'x-sw-page-view-id': '521e097f-e001-4385-a6b6-b6741e7c45dc',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'authority': 'cdn.cookielaw.org',
            'cache-control': 'no-cache',
            'origin': 'https://www.similarweb.com',
            'pragma': 'no-cache',
            'referer': 'https://www.similarweb.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',   
        }

        for key, value in headers.items():
            chrome_options.add_argument(f"--{key}={value}")

        driver = webdriver.Chrome(options=chrome_options)

        home_page = driver.get(f'https://www.similarweb.com/website/{self.__url}/#overview')

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'wa-overview__title'))
        )

        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=current_date.day)
        last_month_name = last_month_date.strftime('%B')
        last_month_year = last_month_date.strftime('%Y')

        last_month = f"{last_month_name}/{last_month_year}"

        try:
            driver.find_element(By.CLASS_NAME, 'error__title').text

            raise ValueError("Requested URL not found: {}".format(self.__url))
        except NoSuchElementException:
            pass

        try:
            try:
                driver.find_element(By.CLASS_NAME, 'app-more-less-text__button').click()
                description_text = driver.find_element(By.CLASS_NAME, 'app-more-less-text').text.replace(' Show less', '')
            except:
                description_text = ""
                pass

            website_data = {
                "title": driver.find_element(By.CLASS_NAME, 'wa-overview__title').text,
                "description": description_text,
                "companyName": driver.find_element(By.CLASS_NAME, 'app-company-info__link').text,
                "yearFounded": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/dl/div[2]/dd').text,
                "employees": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/dl/div[3]/dd').text,
                "headquarter": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/dl/div[4]/dd').text,
                "annual_revenue": "No data",
                "industry": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/dl/div[6]/dd/a').text,
                "country": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[3]/div/div[2]/div/a').text,
                "globalRank": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[3]/div/div[1]/div/p').text,
                "countryRank": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[3]/div/div[2]/p[2]').text,
                "categoryRank": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[3]/div/div[3]/div[1]/p').text,
                "totalVisits": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[4]/div[2]/div[1]/p[2]').text,
                "bounceRate": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[4]/div[2]/div[2]/p[2]').text,
                "pagesPerVisit": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[4]/div[2]/div[3]/p[2]').text,
                "averageVisitDuration": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[4]/div[2]/div[4]/p[2]').text,
                "lastMonthChange": {
                    "change": "",
                    "lastMonth": last_month
                    },
                "topCountries": [],
                "genderDistribution": {
                    "male": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/section[3]/div/div/div[2]/div[2]/ul/li[2]/span[2]').text, 
                    "female": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/section[3]/div/div/div[2]/div[2]/ul/li[1]/span[2]').text
                    },
                "ageDistribution": [],
                "targetAudience": {
                    "topCategories": [],
                    "topTopics": [],
                    "otherVisitedWebsites": []
                },
                "competitorsAndSimilar": [],
                "topTrafficSources": {},
                "trafficShare": {
                    "type": {},
                    "topKeywords": []
                },
                "referralWebTraffic": {
                    "totalReferringWebsites": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[3]/div/div/div[2]/div[2]/div/div[3]/div/span[2]').text,
                    "categoryDistribution": [],
                    "topReferrals": []
                },
                "advertisingTraffic": {
                    "totalPublishers": "",
                    "adNetwork": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[4]/div/div/div[2]/div[1]/div/div[3]/div[2]/span[2]').text,
                    "topPublishers": []
                },
                "socialMediaTraffic": {
                    "socialNetworks": driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[5]/div/div/div[2]/div[1]/div/p[2]').text,
                    "socialMediaDistribution": []
                },
                "OutgoingLinksTrafficShare": {
                    "totalOutgoingLinks": "",
                    "categoryDistribution": [],
                    "topOutgoingLinks": [],
                }
            }

            annual_revenue = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/section/div/div/div/div[5]/div/dl/div[5]/dd').text
            if annual_revenue != '- -': website_data['annual_revenue'] = annual_revenue

            change_web_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/section[1]/div/div/div[3]/div[1]/div[2]/p[2]/span')
            if change_web_element.get_attribute('class').find('down') != -1:
                website_data['lastMonthChange']['change'] = '-' + change_web_element.text
            else:
                website_data['lastMonthChange']['change'] = '+' + change_web_element.text

            top_coutries = driver.find_elements(By.CLASS_NAME, 'wa-geography__country-info')

            for country_element in top_coutries:
                top_country = {
                    "name": country_element.find_element(By.CLASS_NAME, 'wa-geography__country-name').text,
                    "trafficPercentage": country_element.find_element(By.CLASS_NAME, 'wa-geography__country-traffic-value').text,
                }
                try:
                    change_in_percentage = country_element.find_elements(By.TAG_NAME, 'span')[1].text
                    if country_element.find_elements(By.TAG_NAME, 'span')[1].get_attribute('class').find('down') != -1:
                        change_in_percentage = '-' + change_in_percentage
                    else:
                        change_in_percentage = '+' + change_in_percentage

                    top_country['changeInPercentage'] = change_in_percentage
                    if top_country['name'] == 'Others': top_country['changeInPercentage'] = ''
                except IndexError:
                    top_country["changeInPercentage"] = "+0.00%"
                finally: 
                    website_data['topCountries'].append(top_country)

            top_categories_and_topics = driver.find_elements(By.CLASS_NAME, 'wa-interests__chart-item-text')
            other_visited_websites = driver.find_elements(By.CLASS_NAME, 'wa-interests__websites-item-title')
            
            for website in other_visited_websites:
                website_data['targetAudience']['otherVisitedWebsites'].append(website.text)

            for element in top_categories_and_topics:
                if len(website_data['targetAudience']['topCategories']) < 5:
                    website_data['targetAudience']['topCategories'].append(element.text)
                else: website_data['targetAudience']['topTopics'].append(element.text)

            ages_percentages_list = driver.find_elements(By.CLASS_NAME, 'wa-demographics__age-data-label')

            svg_element = driver.find_elements(By.CLASS_NAME, "highcharts-root")[3]

            ages_ranges_container = svg_element.find_elements(By.TAG_NAME, 'g')[14]
            ages_ranges = ages_ranges_container.find_elements(By.TAG_NAME, 'text')

            for index in range(6):
                age_data = {
                    "range": ages_ranges[index].text,
                    "percentages": ages_percentages_list[index].text
                }
                website_data['ageDistribution'].append(age_data)

            competitors_list = driver.find_elements(By.CLASS_NAME, 'wa-competitors__list-item')
            for competitor in competitors_list:
                competitors_and_similar = {
                    'website': competitor.find_element(By.CLASS_NAME, 'wa-competitors__list-item-title').text,
                    'affinity': competitor.find_element(By.CLASS_NAME, 'app-progress').text,
                    'monthlyVisits': competitor.find_elements(By.CLASS_NAME, 'wa-competitors__list-column')[2].text,
                    'category': competitor.find_elements(By.TAG_NAME, 'span')[9].text,
                    'categoryRank': competitor.find_elements(By.TAG_NAME, 'span')[10].text,
                }
                website_data['competitorsAndSimilar'].append(competitors_and_similar)

            svg_element_2 = driver.find_elements(By.CLASS_NAME, "highcharts-root")[4]
            
            traffic_percentages = svg_element_2.find_elements(By.CLASS_NAME, 'wa-traffic-sources__channels-data-label')

            traffic_sources = {
                "direct": traffic_percentages[0].text,
                "referrals": traffic_percentages[1].text,
                "organicSearch": traffic_percentages[2].text,
                "paidSearch": traffic_percentages[3].text,
                "social": traffic_percentages[4].text,
                "mail": traffic_percentages[5].text,
                "display": traffic_percentages[6].text,
            }
            website_data['topTrafficSources'] = traffic_sources

            traffic_share_types = driver.find_elements(By.CLASS_NAME, 'wa-keywords__organic-paid-legend-item-title')
            traffic_share_types_percentage = driver.find_elements(By.CLASS_NAME, 'wa-keywords__organic-paid-legend-item-value')

            type = {
                traffic_share_types[0].text: traffic_percentages[0].text,
                traffic_share_types[1].text: traffic_percentages[1].text,
            }
            website_data['trafficShare']['type'] = type

            top_keywords_containers = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[2]/div/div/div[2]/div/div/div[1]').find_elements(By.CLASS_NAME, 'wa-vectors-list__item')
            top_keywords_containers.pop(-1)

            for keyword in top_keywords_containers:
                keyword = {
                    'keyword': keyword.find_element(By.CLASS_NAME, 'wa-vectors-list__item-title').text,
                    'usage': keyword.find_element(By.CLASS_NAME, 'wa-vectors-list__item-value').text,
                    'volume': keyword.find_element(By.CLASS_NAME, 'wa-vectors-list__item-subtitle').text.replace('VOL: ', ''),
                    'price': keyword.find_element(By.CLASS_NAME, 'wa-vectors-list__item-sub-value').text
                }
                website_data['trafficShare']['topKeywords'].append(keyword)

            total_keywords = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[2]/div/div/div[2]/div/div/div[3]/div/span[2]').text
            website_data['trafficShare']['totalKeywords'] = total_keywords

            category_distribution_list = driver.find_elements(By.CLASS_NAME, 'wa-category-distribution__item')

            for category_distribution in category_distribution_list:
                category_name = category_distribution.find_elements(By.TAG_NAME, 'span')[0].text
                category_percentage = category_distribution.find_elements(By.TAG_NAME, 'span')[1].text

                if (category_name.find('%') != -1): 
                    category_name = category_distribution.find_element(By.TAG_NAME, 'p').text
                    category_percentage = category_distribution.find_element(By.TAG_NAME, 'span').text
                
                category = {
                    "name": category_name,
                    "percentage": category_percentage
                }
                website_data['referralWebTraffic']['categoryDistribution'].append(category)

            top_referrals_list = driver.find_elements(By.CLASS_NAME, 'wa-vectors-list__items')[1].find_elements(By.TAG_NAME, 'a')

            for index in range(7):
                try:
                    current_referral_spans = top_referrals_list[index].find_elements(By.TAG_NAME, 'span')
                    referral = {}

                    if index <= 2 or index == 6:
                        referral['name'] = current_referral_spans[1].text
                        referral['percentage'] = current_referral_spans[2].text
                    else:
                        referral['name'] = current_referral_spans[4].text
                        referral['percentage'] = current_referral_spans[5].text

                    if referral['name'] == 'Start a trial': referral['name'] = "Unknown"
                    website_data['referralWebTraffic']['topReferrals'].append(referral)
                except IndexError: 
                    break

            total_publishers = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[5]/section[4]/div/div/div[2]/div[1]/div/div[3]/div[1]/span[2]').text

            if total_publishers.find("\n") != -1: 
                website_data['advertisingTraffic']['totalPublishers'] = total_publishers.replace("\n", " ")
            else:
                website_data["advertisingTraffic"]['totalPublishers'] = total_publishers

            advertising_traffic_list = driver.find_elements(By.CLASS_NAME, 'wa-vectors-list__items')[2].find_elements(By.TAG_NAME, 'a')

            if len(advertising_traffic_list) > 0: 
                for index in range(6):
                    try:
                        current_ad_traffic_spans = advertising_traffic_list[index].find_elements(By.TAG_NAME, 'span')
                        ad_traffic = {}
                        if index <= 1 or index == 5:
                            ad_traffic['website'] = current_ad_traffic_spans[1].text
                            ad_traffic['percentage'] = current_ad_traffic_spans[2].text
                        else:
                            ad_traffic['website'] = current_ad_traffic_spans[4].text
                            ad_traffic['percentage'] = current_ad_traffic_spans[5].text

                        if ad_traffic['website'] == 'Start a trial': ad_traffic['website'] = "Unknown"
                        website_data['advertisingTraffic']['topPublishers'].append(ad_traffic)
                    except IndexError:
                        break

            svg_element_3 = driver.find_elements(By.CLASS_NAME, "highcharts-root")[6]

            social_media_percentages_list = svg_element_3.find_elements(By.TAG_NAME, 'tspan')

            social_media_list = driver.find_elements(By.CLASS_NAME, 'wa-social-media__chart-label-title')

            for index in range(6):
                try:
                    percentage = social_media_percentages_list[index].text
                    social_media = {
                        "name": social_media_list[index].text,
                        "percentage": percentage
                    }
                    website_data['socialMediaTraffic']['socialMediaDistribution'].append(social_media)
                except IndexError:
                    break

            total_outgoing_links = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[6]/section/div/div/div[2]/div[1]/div/div[2]/div/span[2]').text

            if total_outgoing_links.find("\n") != -1:
                website_data["OutgoingLinksTrafficShare"]['totalOutgoingLinks'] = total_outgoing_links.replace("\n", " ")
            else:
                website_data["OutgoingLinksTrafficShare"]['totalOutgoingLinks'] = total_outgoing_links

            category_distribution_list = driver.find_elements(By.CLASS_NAME, 'wa-category-distribution__list')[1].find_elements(By.CLASS_NAME, 'wa-category-distribution__item')

            for index in range(5):
                try:
                    current_category = category_distribution_list[index]
                    category = {
                        "name": current_category.find_elements(By.TAG_NAME, 'span')[0].text,
                        "percentage": current_category.find_elements(By.TAG_NAME, 'span')[1].text
                    }
                    website_data['OutgoingLinksTrafficShare']['categoryDistribution'].append(category)
                except IndexError:
                    break

            top_outgoing_link_list = driver.find_elements(By.CLASS_NAME, 'wa-vectors-list__items')[3].find_elements(By.TAG_NAME, 'a')

            for index in range(7):
                try:
                    current_outgoing_link_spans = top_outgoing_link_list[index].find_elements(By.TAG_NAME, 'span')
                    outgoing_link = {}
                    if len(current_outgoing_link_spans) == 3 or index == 6:
                        outgoing_link['name'] = current_outgoing_link_spans[1].text
                        outgoing_link['percentage'] = current_outgoing_link_spans[2].text
                    else:
                        outgoing_link['name'] = current_outgoing_link_spans[4].text
                        outgoing_link['percentage'] = current_outgoing_link_spans[5].text

                    if outgoing_link['name'] == 'Start a trial': outgoing_link['name'] = "Unknown"
                    website_data['OutgoingLinksTrafficShare']['topOutgoingLinks'].append(outgoing_link)
                except IndexError:
                    break

            return website_data
        except Exception as e:
            print(str(e))
            raise Exception('500: Internal Server Error')