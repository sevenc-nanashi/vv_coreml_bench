import time
import asyncio
import ctypes

ctypes.CDLL("./libonnxruntime.1.14.0.dylib")
import voicevox_core


async def main():
    open_jtalk = voicevox_core.OpenJtalk("./open_jtalk_dic_utf_8-1.11")
    conv1d = await voicevox_core.VoiceModel.from_path("./conv1d.vvm")
    conv2d = await voicevox_core.VoiceModel.from_path("./conv2d.vvm")

    for acceleration in [
        voicevox_core.AccelerationMode.CPU,
        voicevox_core.AccelerationMode.GPU,
    ]:
        synthesizer = await voicevox_core.Synthesizer.new_with_initialize(
            open_jtalk, acceleration_mode=acceleration
        )
        if acceleration == voicevox_core.AccelerationMode.CPU:
            print("CPU:")
        else:
            print("GPU:")

        for name, model in [("conv1d", conv1d), ("conv2d", conv2d)]:
            await synthesizer.load_voice_model(model)

            results = []
            for i in range(10):
                start = time.time()
                await synthesizer.tts(
                    f"おーる ゆあ ぼいしーず あー びろんぐ つー あす", model.metas[0].styles[0].id
                )
                results.append(time.time() - start)

            print(f"  {name}:")
            print(f"    mean: {sum(results) / len(results)}")
            print(f"    min: {min(results)}")
            print(f"    max: {max(results)}")

            synthesizer.unload_voice_model(model.id)


if __name__ == "__main__":
    asyncio.run(main())
