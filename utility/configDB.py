from envManager import save_to_env

save_to_env("DB_NAME", input("name db: "))
save_to_env("DB_USER", input("user: "))
save_to_env("DB_PASSWORD", input("password: "))
save_to_env("DB_HOST", input("host ip: "))