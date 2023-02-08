import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naukri.com/job-listings-senior-data-science-and-analytics-strategy-consultant-wells-fargo-international-solutions-private-ltd-hyderabad-secunderabad-5-to-7-years-060223906080?src=discovery_trendingWdgt_homepage_srch&sid=16758771956441791&xp=1&px=1')

soup = BeautifulSoup(res.text,features="html.parser")

jobTitle = soup.find('h1',{'class':'av-special-heading-tag','itemprop':'headline'}).text
jobDiscription = soup.find('div',{'class':"clearboth description"}) #multiple child tages inside
moreInfo = soup.findAll('p',{'class':"coPE"})
keySkills = soup.find('div',{'class':'getJobKeySkillsSection key-skill'}) #multiple child tages inside
companyProfile = soup.find('section',{'class':"getCompanyProfile JD av_textblock_section companyprofilesection about-company jDisc mt25"}) #multiple child tages inside

print('Job Title :',jobTitle)

print('Job Discription')
for dis in jobDiscription:
    print(dis.text)

print()
for info in moreInfo:
    print(info.text)

print()
for skill in keySkills:
    try:
        for s in skill:
            print(s.text)
    except:
        print(skill.text)

print()
for cpro in companyProfile:
    print(cpro.text)


