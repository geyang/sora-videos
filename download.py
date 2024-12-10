import os
import requests

def download_files(urls, save_dir="downloads"):
    """
    Downloads files from a list of URLs and saves them to a specified directory.

    Args:
        urls (list): List of URLs to download.
        save_dir (str): Directory where files will be saved. Default is 'downloads'.

    Returns:
        None
    """
    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    for url in urls:
        try:
            # Get the file name from the URL
            filename = os.path.basename(url.split("?")[0])  # Handle query params
            save_path = os.path.join(save_dir, filename)

            # Download the file
            print(f"Downloading {url}...")
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise HTTPError for bad responses

            # Write the content to a file
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Saved to {save_path}")
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    # Example list of URLs
    url_list =  [
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqn34zjfahtcanczhepy9sj%2Ftask_01jeqn34zjfahtcanczhepy9sj_genid_538ee9f6-c3ee-4882-8066-38e18645ef2a_24_12_10_06_46_711127%2Fvideos%2F00000_321805.mp4%2Fmd.mp4?st=2024-12-10T06%3A48%3A01Z&se=2024-12-16T07%3A48%3A01Z&sks=b&skt=2024-12-10T06%3A48%3A01Z&ske=2024-12-16T07%3A48%3A01Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=ZzdlADA25eWw8lIomH6yAKFMtYfFcEaki3CUlJvnwCw%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqn3b0rf5kaseht6zby3wh3%2Ftask_01jeqn3b0rf5kaseht6zby3wh3_genid_dc40748c-6bd7-45c2-8194-d720c715e90e_24_12_10_06_46_944811%2Fvideos%2F00000_664675.mp4%2Fmd.mp4?st=2024-12-10T05%3A52%3A46Z&se=2024-12-16T06%3A52%3A46Z&sks=b&skt=2024-12-10T05%3A52%3A46Z&ske=2024-12-16T06%3A52%3A46Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=aWErtadtID23QoKMKPf8vXfq2j%2BWqTNDmzr46%2BRI0KU%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqn2y3nfewrnew0e3gm0mtd%2Ftask_01jeqn2y3nfewrnew0e3gm0mtd_genid_04d820e6-f0dc-42bb-b379-7f412e033e80_24_12_10_06_46_988905%2Fvideos%2F00000_126562.mp4%2Fmd.mp4?st=2024-12-10T07%3A40%3A25Z&se=2024-12-16T08%3A40%3A25Z&sks=b&skt=2024-12-10T07%3A40%3A25Z&ske=2024-12-16T08%3A40%3A25Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=JMu13kpc%2F4Gp6iyeMKyXCzu8obHXAUQFuKwOR6EYre0%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqn3h8efxgst3kq1ma6nbnv%2Ftask_01jeqn3h8efxgst3kq1ma6nbnv_genid_04083e34-bd27-4c1c-9949-de5d6f770ce9_24_12_10_06_46_656260%2Fvideos%2F00000_21059.mp4%2Fmd.mp4?st=2024-12-10T07%3A40%3A25Z&se=2024-12-16T08%3A40%3A25Z&sks=b&skt=2024-12-10T07%3A40%3A25Z&ske=2024-12-16T08%3A40%3A25Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=4v5UMNWa44EnnOyedBf2kXsUXBOBsUUvlkTLpdQBiKM%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqn483wejbs87w2ttdhzkt3%2Ftask_01jeqn483wejbs87w2ttdhzkt3_genid_cff400c2-928d-4dd8-91bc-3e45799823e3_24_12_10_06_47_742996%2Fvideos%2F00000_500166.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A33Z&se=2024-12-16T07%3A46%3A33Z&sks=b&skt=2024-12-10T06%3A46%3A33Z&ske=2024-12-16T07%3A46%3A33Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=Vad%2BE6KzmALuiSD7rBVovk59%2F%2FqZoCsIQMULKe7Ab1s%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmft71ewra8dxsnwrka74n%2Ftask_01jeqmft71ewra8dxsnwrka74n_genid_6fc882f2-06a9-41a4-88f9-4f5a8d6f3e74_24_12_10_06_36_756248%2Fvideos%2F00000_358839.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A11Z&se=2024-12-16T07%3A46%3A11Z&sks=b&skt=2024-12-10T06%3A46%3A11Z&ske=2024-12-16T07%3A46%3A11Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=SKBvbjXqXwkC9CvivDbcogkS1bdVWATS06hL6k0o3DY%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmgh23etbr8a5dc7xrzf14%2Ftask_01jeqmgh23etbr8a5dc7xrzf14_genid_518aa012-294e-460f-a6ba-d1344e8a2370_24_12_10_06_36_535850%2Fvideos%2F00000_475060.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A11Z&se=2024-12-16T07%3A46%3A11Z&sks=b&skt=2024-12-10T06%3A46%3A11Z&ske=2024-12-16T07%3A46%3A11Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2Fxkc3CYTvb6Fr5ZiTWIiA5MWiG0FZx%2F5cOQqAwlS9zk%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqme4hkfp0tj1g765b8462r%2Ftask_01jeqme4hkfp0tj1g765b8462r_genid_321ccb05-17cf-434d-9fcd-041c493ade4e_24_12_10_06_36_345603%2Fvideos%2F00000_420073.mp4%2Fmd.mp4?st=2024-12-10T06%3A45%3A30Z&se=2024-12-16T07%3A45%3A30Z&sks=b&skt=2024-12-10T06%3A45%3A30Z&ske=2024-12-16T07%3A45%3A30Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=myD3QCqE7ojQ4aYdE579OEQ2Pmj46rXd96lkZRIY3KM%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmgmw1e95tj6yq432kmx7q%2Ftask_01jeqmgmw1e95tj6yq432kmx7q_genid_741c5320-4e58-43cc-86ca-3bbbf05cb555_24_12_10_06_36_044332%2Fvideos%2F00000_893391.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A11Z&se=2024-12-16T07%3A46%3A11Z&sks=b&skt=2024-12-10T06%3A46%3A11Z&ske=2024-12-16T07%3A46%3A11Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=lN%2FxguKqbmyj%2BR5XcGHrkPljHEmMhQrGoebhaQRtYyU%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmdkxsfay8cmr71hh5y9sx%2Ftask_01jeqmdkxsfay8cmr71hh5y9sx_genid_ed7b73ea-fd7f-497c-959e-f11fc0e9b894_24_12_10_06_35_201604%2Fvideos%2F00000_382995.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A11Z&se=2024-12-16T07%3A46%3A11Z&sks=b&skt=2024-12-10T06%3A46%3A11Z&ske=2024-12-16T07%3A46%3A11Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2F4uEYdqCC93Vpv5GWat1LQ87nNdCjybbbdYAGrKwPI4%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmh8bkeyz9gnak2vqt2924%2Ftask_01jeqmh8bkeyz9gnak2vqt2924_genid_4999a5a5-51be-48eb-9820-6a25bd0172ac_24_12_10_06_36_435402%2Fvideos%2F00000_730566.mp4%2Fmd.mp4?st=2024-12-10T06%3A48%3A01Z&se=2024-12-16T07%3A48%3A01Z&sks=b&skt=2024-12-10T06%3A48%3A01Z&ske=2024-12-16T07%3A48%3A01Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=1%2FImvFegdauHsM7UXFOl4hDGESi6QIDKMt5lxuLgG6U%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmgngfe20s6sgk91rk214q%2Ftask_01jeqmgngfe20s6sgk91rk214q_genid_e365a04e-25eb-4211-854a-f5b1390816bf_24_12_10_06_36_793748%2Fvideos%2F00000_76887.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A11Z&se=2024-12-16T07%3A46%3A11Z&sks=b&skt=2024-12-10T06%3A46%3A11Z&ske=2024-12-16T07%3A46%3A11Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=xa08dH4LxUOBC8joly1ccmUkpJM0Pm5d%2FnsjzXy0neE%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmht5kfscsttfq0x4bdeea%2Ftask_01jeqmht5kfscsttfq0x4bdeea_genid_17c80772-ec8a-4e7d-be96-42f4c1810ca5_24_12_10_06_37_002386%2Fvideos%2F00000_584247.mp4%2Fmd.mp4?st=2024-12-10T06%3A46%3A52Z&se=2024-12-16T07%3A46%3A52Z&sks=b&skt=2024-12-10T06%3A46%3A52Z&ske=2024-12-16T07%3A46%3A52Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=%2FNm2SLB8dBcijgI36zH7N%2BVdyj6g49tKWH3QwCyXy3c%3D&az=oaivgprodscus",
        "https://videos.openai.com/vg-assets/assets%2Ftask_01jeqmhhr6fdkanx7330cj59pe%2Ftask_01jeqmhhr6fdkanx7330cj59pe_genid_8f321ebd-b200-4c81-aea3-2a107ad6d227_24_12_10_06_37_219084%2Fvideos%2F00000_315406.mp4%2Fmd.mp4?st=2024-12-10T06%3A47%3A37Z&se=2024-12-16T07%3A47%3A37Z&sks=b&skt=2024-12-10T06%3A47%3A37Z&ske=2024-12-16T07%3A47%3A37Z&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skoid=8ebb0df1-a278-4e2e-9c20-f2d373479b3a&skv=2019-02-02&sv=2018-11-09&sr=b&sp=r&spr=https%2Chttp&sig=LSOcn60umHKXX3AK2YrR81Dd7NEl9qSe%2BU2J%2B5zFgVQ%3D&az=oaivgprodscus"
    ]

    # Call the function with the list of URLs
    download_files(url_list)

