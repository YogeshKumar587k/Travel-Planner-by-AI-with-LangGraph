#from tools.tavily_tool import tavily_search
#from tools.flight_tool import search_flights
#res=tavily_search("best hotels in India")

#print(res)
#print(search_flights("Plan a 2 days bangalore trip from chennai"))

from backend import run_travel_agent

user_input = input("Enter your travel query: ")

response = run_travel_agent(user_input,thread_id="test_user")


print("Answer:", response["answer"])