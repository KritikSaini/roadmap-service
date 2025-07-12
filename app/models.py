from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)



from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Workspace(Base):
    __tablename__ = "workspaces"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    progress = Column(Integer)
    prior_knowledge = Column(String)  # comma-separated list
    root_node = Column(Integer, ForeignKey("map_nodes.id"))



class MapNode(Base):
    __tablename__ = "map_nodes"
    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    epic = Column(String)
    content_resource = Column(String)
    child_nodes = Column(String)  # comma-separated node IDs
    is_completed = Column(String)



class QuestionAnswer(Base):
    __tablename__ = "question_answers"
    id = Column(Integer, primary_key=True, index=True)
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))
    question = Column(String)
    answer = Column(String)
