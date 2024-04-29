import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div>
      <div className='p-3 max-w-5xl mx-auto'>
        <h1 className="text-3xl font-semibold text-center my-7">Welcome to Heartility!</h1>
            We will analyze, predict the result whether the patient has heart disease or normal, i.e. Heart disease prediction using Machine Learning.
      </div>
      <div className='flex'>
        <div>
          
        </div>
        <div className='p-3 max-w-lg mx-auto'>
          <Link to='/predict'>
            <button className="bg-slate-700 text-white rounded-lg p-3 uppercase hover:opacity-90  ">Predict Now!</button>
          </Link>
        </div>
        <div>
          
        </div>
      </div>
    </div>
  )
}
