"""
Homework 2 | Question 2
Name       | Noga Zohar
ID         | 313263485
"""

# imports
from enum import Enum
from collections import namedtuple

Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

# type check function
def type_check(first_agent, second_agent):
    """
    Compare types (categories) of two different agents.

    Parameters
    ----------
    first_agent, second_agent : two Agent objects

    Returns
    -------
    first_agent, second_agent : two Agent objects, changed 
    """
    # get category value
    first_status = first_agent.category.value
    second_status = second_agent.category.value
    
    # both agents are CURE
    if first_status == 1 and second_status == 1:
       pass 
    # first agent is CURE
    elif first_status == 1:
        second_agent = Agent(second_agent.name, Type(second_status-1))
    # second agent is CURE
    elif second_status == 1:
        first_agent = Agent(first_agent.name, Type(first_status-1))
    # no agent is CURE
    else:
        first_agent = Agent(first_agent.name, Type(first_status+1))
        second_agent = Agent(second_agent.name, Type(second_status+1))
    
    return first_agent, second_agent
    
# main function
def meetup(agent_listing: tuple) -> list:
    """
    Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    
    # variables
    attend_values = [1,3,4] # category values for those attending meetings
    # not_attend = [2, 5]     # category values for those not attending meetings
    attendees = [x for x in agent_listing if x.category.value in attend_values]
    updated_listing = [x for x in agent_listing if x.category.value not in attend_values] # output list

    # meetings loop
    for i in range(0,len(attendees)-1,2):
        # call function type_check
        first_agent, second_agent = type_check(attendees[i], attendees[i+1])
        # add changed agents to output list
        updated_listing.append(first_agent)
        updated_listing.append(second_agent)

    # for an odd number of agents, append solo agent
    if len(attendees)%2:
        updated_listing.append(attendees[-1])
    
    return updated_listing