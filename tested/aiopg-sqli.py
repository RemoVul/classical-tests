import asyncio
import asyncpg

def bad1():
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = "SELECT name FROM users WHERE age=" + req.FormValue("age")
    await cur.execute(query)

async def bad2():
    pool = await aiopg.create_pool(dsn)

    with (await pool.cursor()) as cur:
        sql_query = 'SELECT * FROM {}'.format(user_input)
        await cur.execute(sql_query)
        ret = await cur.fetchone()
        assert ret == (1,), ret

def bad3(user_input):
    pool = await aiopg.create_pool(dsn)
    async with pool as conn:
        cur = await conn.cursor()
        sql_query = f'SELECT * FROM {user_input}'
        await cur.execute(sql_query)

def bad4():
    pool = await aiopg.create_pool(dsn)
    async with pool.cursor() as cur:
        await cur.execute("SELECT name FROM users WHERE age=" + req.FormValue("age"))

def bad5(user_input):
    pool = await aiopg.create_pool(dsn)
    async with pool.cursor() as cur:
        await cur.execute('SELECT * FROM {}'.format(user_input))

async def bad6(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute('SELECT * FROM %s'%(user_input))

async def bad7(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute(f'SELECT * FROM {user_input}')

def ok1(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute("SELECT * FROM test WHERE id = %s", (3,))

def ok2(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = "SELECT name FROM users WHERE age=" + "3"
    cur.execute(query)

def ok3(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = "SELECT name FROM users WHERE age="
    query += "3"
    cur.execute(query)

def ok4(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = 'SELECT * FROM John'.format()
    cur.fetchval(query)

def ok5(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = 'SELECT * FROM John'% ()
    cur.execute(query)

def ok6(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    query = f'SELECT * FROM John'
    cur.execute(query)

def ok7(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute("SELECT name FROM users WHERE age=" + "3")

def ok8(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute('SELECT * FROM John'.format())

def ok9(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute('SELECT * FROM John'% ())

def ok10(user_input):
    conn = await aiopg.connect(database='aiopg',
                               user='aiopg',
                               password='secret',
                               host='127.0.0.1')
    cur = await conn.cursor()
    cur.execute(f'SELECT * FROM John')
