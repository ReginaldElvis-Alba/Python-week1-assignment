const mysql=require('mysql2')
const dotenv=require('dotenv')
dotenv.config();
let instance=null;

const connection= mysql.createConnection({
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || 'Konshens1',
    database: process.env.DB_NAME || 'web_app',
    port: process.env.DB_PORT || 3306
    
});

connection.connect((err) =>{
    if(err){
        console.log('Connection error',err.message)
    }
    console.log('database connected succefully',);
});

class DbService{
    static getDbServiceInstance(){
        return instance ? instance : new DbService();
    }
    async getAllData(){
        try{
            const response = await new Promise((resolve, reject)=>{
                const query = "SELECT * FROM names ";

                connection.query(query, (err, results)=>{
                    if (err)reject (new Error(err.message));
                    resolve(results);
                })
            });
           // console.log(responce)
            return responce;

        }catch(error){
            console.log(error)
        }
    }
}
module.exports= DbService;