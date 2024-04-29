export default function Predict() {
  return (
    <div>
      <div className='p-3 max-w-6xl mx-auto'>
        <iframe
          src="https://heartility.streamlit.app/?embed=true"
          height="820"
          style={{ width: "100%", border: "none"}}
        ></iframe>
      </div>
    </div>
  )
}
