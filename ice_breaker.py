import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

#llm models
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


information = """
LeBron Raymone James Sr. (/ləˈbrɒn/;[1] lə-BRON; born December 30, 1984) is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA). Nicknamed "King James," he is widely regarded as one of the greatest basketball players of all time, and is frequently at the center of debates regarding the sport's all-time best, often being compared to Michael Jordan.[a] James has won four NBA championships from 10 NBA Finals appearances, having made eight consecutive appearances between 2011 and 2018.[2] He also won the inaugural NBA Cup in 2023 with the Lakers, three Olympic gold medals as a member of the U.S. national team, and the Olympics MVP in the 2024 Summer Olympics.

In addition to being the NBA's all-time leading scorer and ranking fourth in NBA career assists and eighth in NBA career steals, James holds several individual honors: four NBA Most Valuable Player (MVP) Awards, four NBA Finals MVP Awards, the NBA Rookie of the Year Award, three NBA All-Star Game MVP Awards, and the inaugural NBA Cup MVP award. He has been named an NBA All-Star a record 20 times, selected to the All-NBA Team a record 20 times (including a record 13 First Team selections)[3][4] and the All-Defensive Team six times (including five First Team selections), and was a runner-up for the NBA Defensive Player of the Year Award twice in his career.[5][6] The oldest active player in the NBA, he is tied with Vince Carter for the record for the most seasons played in NBA history, with 22, and holds the record for the most minutes played in NBA history. [7]

James grew up playing basketball for St. Vincent–St. Mary High School in his hometown of Akron, Ohio. He was heavily touted by the national media as a future NBA superstar for his all-around scoring, passing, athleticism and playmaking abilities.[8] A prep-to-pro, James was selected by the Cleveland Cavaliers with the first overall pick of the 2003 NBA draft. Named the 2004 NBA Rookie of the Year,[9] he soon established himself as one of the league's premier players, leading the Cavaliers to their first NBA Finals appearance in 2007 and winning the NBA MVP award in 2009 and 2010.[5] James left in 2010 as a free agent to join the Miami Heat;[10] this was announced in a nationally televised special titled The Decision and is among the most controversial free agency moves in sports history.

James won his first two NBA championships while playing for the Heat in 2012 and 2013; in both of these years, he additionally earned the league's MVP and Finals MVP awards. After his fourth season with the Heat in 2014, James opted out of his contract and returned to the Cavaliers. In 2016, he led the Cavaliers to victory over the Golden State Warriors in the Finals by coming back from a 3–1 deficit, delivering the team's first championship, ending the Cleveland sports curse, and winning his third Finals MVP.[11] In 2018, James exercised his contract option to leave the Cavaliers and signed with the Lakers, where he won the 2020 NBA championship and his fourth Finals MVP.[12] On February 7, 2023, James surpassed Kareem Abdul-Jabbar to become the leading scorer in league history, and the following year, he became part of the first father-son teammate duo in NBA history, playing alongside his son Bronny with the Lakers.

Off the court, James has earned further wealth and fame from numerous endorsement contracts. He is the first player in NBA history to accumulate $1 billion in earnings as an active player.[13] James has been featured in books, documentaries (including winning three Sports Emmy Awards as an executive producer), and television commercials. He was among Time's 100 most influential people in the world in 2005, 2013, 2017, and 2019 – the most selections for a professional athlete. James has won 20 ESPY Awards, hosted Saturday Night Live, and starred in the sports film Space Jam: A New Legacy (2021). He has been a part-owner of Liverpool F.C. since 2011 and leads the LeBron James Family Foundation, which has opened an elementary school, housing complex, retail plaza, and medical center in Akron, Ohio.[14][15]
"""

if __name__ == '__main__':
    print("asdjasd")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-pro")
    #llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information":information})

    print(res)