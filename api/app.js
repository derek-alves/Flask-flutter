import gtfs from 'gtfs';


const config = {
    "agencies": [
      {
        "path": "./assets/1gtfs.zip"
      }
    ]
  }


const upload = async ()=>{
    try {
        await gtfs.import(config);
        console.log("foi");
    } catch (error) {
        console.log("não foi");
    }
    
}

upload();

