from fastapi import FastAPI
from routers.user_router import router as user_router
from db.database import Base, engine
from routers.prodect_router import router as prodect_router
from routers.category_routers import router as catagory_router
from routers.volunteer_router import router as volunteer_router
from routers.camp_router import router as camp_router
from routers.cart_routers import router as cart_routers
from routers.order_router import router as order_router

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(prodect_router)


app.include_router(user_router)

app.include_router(catagory_router)

app.include_router(volunteer_router)

app.include_router(camp_router)

app.include_router(cart_routers)

app.include_router(order_router)