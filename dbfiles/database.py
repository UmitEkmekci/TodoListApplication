from sqlalchemy import create_engine # Database motoru
from sqlalchemy.orm import declarative_base # Database'de modelleri kurmak için gerekli olan class
from sqlalchemy.orm import sessionmaker # Database işlemlerini uygulayabilmek için gereken session'ı oluşturur.



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/todo" # Postgresql bağlantısı kurabilmek için, kullanılacak olan postgre database linki tanımlanır.Linkin için kullanılan değerler sırasıyla; postgres: username, admin: şifre, localhost: host, postgres: database_name
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Engine kullanılarak, database motoru ilgili database linki ile başlatılır.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Sessionmaker ile motoru çalıştırılan database'e (bind=engine) session oluşturuluyor.
Base = declarative_base() # declerative base class'ı, model oluşturabilmemizi sağlayan ana class'tır. 