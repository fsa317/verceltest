export const config = {
    runtime: "edge",
  };
  
  const handler = async (req: Request): Promise<Response> => {
    console.log("test edge function called");
    return new Response("test");
  }

  export default handler;