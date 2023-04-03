import React, { useContext, useState, useEffect } from 'react'


const HomePage = () => {

    const [urls, setUrls] = useState("")
    const [websites, setWebsites] = useState("")

    const [onlyWebsites, setOnlyWebsites] = useState("")

    const [timeTotal, setTimeTotal] = useState("")

    const [urlfilter, setUrlFilter] = useState("")


    const getUrls = async () => {
    
       
        const response = await fetch(`https://web-tracker-hhjh.onrender.com/new-tab-filter?url=${urlfilter}`,
    
        {
          method: 'GET',
          credentials: "include",
          headers: {
            "Content-Type": "application/json"
          },
          
        
        }
        )
        const data = await response.json()

        setUrls(data)
        const timess = []
        
        
         for (const i in data){
            //console.log(data[i].diff)
          

            timess.push(data[i].diff)
            

            //const times = timess.slice(0, -1)
            const times = timess
            console.log(times)

            const z = (n) => (n < 10 ? '0' : '') + n;
        
            let hour = 0
            let minute = 0
            let second = 0
            for (const time of times) {
                const splited = time.split(':');
                hour += parseInt(splited[0]);
                minute += parseInt(splited[1])
                second += parseInt(splited[2])
            }
            const seconds = second % 60
            const minutes = parseInt(minute % 60) + parseInt(second / 60)
            const hours = hour + parseInt(minute / 60)
        
             setTimeTotal((hours) + ':' + z(minutes) + ':' + z(seconds))


         }


        




         const newData = [...new Set(data.map(data => (data.url)))]

         setWebsites(newData)
         //console.log(newData)
        
        
        
        
    
       //console.log(data)
    
      }



      const getOnlyUrls = async () => {
    
       
        const response = await fetch(`https://web-tracker-hhjh.onrender.com/new-tab-filter`,
    
        {
          method: 'GET',
          credentials: "include",
          headers: {
            "Content-Type": "application/json"
          },
          
        
        }
        )
        const data = await response.json()

       

         const newData = [...new Set(data.map(data => (data.url)))]

         setOnlyWebsites(newData)
         //console.log(newData)
        
        
        
        
    
       //console.log(data)
    
      }

      console.log(urlfilter)


      
    
      useEffect(() => {
		getUrls()
    getOnlyUrls()
    
    //getListingsFilter()
	  }, [])


 
    

    return (
        <div class="row">
          
        

            
            {websites && websites.map((website, index)=>(
		<React.Fragment key = {index}>
			
			
			<div className=''>
        
      
     
              {urls && urls.map((url, index)=>(
		<React.Fragment key = {index}>
			{timeTotal !== "NaN:NaN:NaN"?
			
			<div className='time'>
        {url.url==`${website}`?
        
             <h1>{timeTotal}</h1>
        :null}
              {
                  
                } 
			</div>
       :null }

		</React.Fragment>
		))[0]}

          
    
           
			</div>
		</React.Fragment>
		))}
    




{onlyWebsites && onlyWebsites.map((onlyWebsite, index)=>(
		<React.Fragment key = {index}> 

        
{onlyWebsite =="localhost:3000" ? null :
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        
        <h5 class="card-title"><p>{onlyWebsite}</p></h5>
        <a  onClick={ ()  => {setUrlFilter(onlyWebsite);getUrls()}} href="#" class="btn btn-primary">Get Time</a>
      </div>
    </div>
  </div>
  
     
}
           
			
		</React.Fragment>
		))}



  
                
            </div>

    )
}
export default HomePage